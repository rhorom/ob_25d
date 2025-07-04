import ee
from tqdm import tqdm

'''
Script to process and download building characteristics based on
the Google Open Buildings 2.5D.

See: Priyatikanto et al., A 100-m resolution building characteristics 
for the Global South derived from Google Open Buildings Temporal 
dataset 2016-2023
'''

ee.Authenticate()
ee.Initialize(project='your-project-name')

region = ee.Geometry.BBox(-120.000000096,-60.999975942,145.000000014,40.000000176)
band = input('select band [count, perimeter, surface, volume, distance]: ')
year = input('select year [2016-2023]: ')

crsTransform = [0.00083333333, 0, -179.999999856, 0, -0.00083333333, 84.0]
#crsTransform = [0.00083333333, 0, -120.000000096, 0, -0.00083333333, 40.000000176]

def exportFunc(image, region, desc):
  task = ee.batch.Export.image.toDrive(
      image=image,
      region=region,
      description=desc,
      folder='v4_'+year,
      crs='EPSG:4326',
      crsTransform=crsTransform,
      maxPixels=1e12,
      shardSize=256,
      fileDimensions=65536
  )
  task.start()
  #print(desc)

def mainFunc(idx):
  desc = band + '_t4_' + idx

  img = imcol.filter(ee.Filter.eq('system:index', idx)).first()
  mask = img.select('building_presence').gt(0.4)
  img = img.updateMask(mask)
  reg = img.geometry()

  if (band == 'count'):
    out = (img.select('building_fractional_count')
      .reduceResolution(reducer='sum', maxPixels=1024, bestEffort=True)
      .reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .multiply(4e4).uint16()
      .rename('building_count'))
  elif (band == 'surface'):
    out = (mask.toFloat()
      .reduceResolution(reducer='sum', maxPixels=1024, bestEffort=True)
      .reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .multiply(1e4).uint16()
      .rename('building_surface'))
  elif (band == 'volume'):
    #building volume is in 10 m^3
    out = (img.select(['building_height'])
      .reduceResolution(reducer='sum', maxPixels=1024, bestEffort=True)
      .reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .multiply(1e3).uint16()
      .rename('building_volume'))
  elif (band == 'perimeter'):
    out = (mask.convolve(ee.Kernel.laplacian8(normalize=True)).gt(0)
        .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
        .reproject(crs='EPSG:4326', crsTransform=crsTransform)
        .multiply(2e3).int16()
        .rename('building_perimeter'))
  elif (band == 'distance'):
    #building_distance is in cm
    kernel = ee.Kernel.euclidean(radius=400, units='meters', normalize=False)
    out = (mask.distance(kernel)
        #.reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
        #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
        .subtract(566).multiply(-100).uint16()
        .rename('building_distance'))
  elif (band == 'varh'):
    fct = img.select('building_fractional_count')#.gt(0.002) #better without thresholding
    prb = (fct
        .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
        .reproject(crs='EPSG:4326', crsTransform=crsTransform))
    h1 = (img.select('building_height').pow(2)
        .multiply(fct)
        .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
        .reproject(crs='EPSG:4326', crsTransform=crsTransform)
        .divide(prb))

    h2 = (img.select('building_height')
        .multiply(fct)
        .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
        .reproject(crs='EPSG:4326', crsTransform=crsTransform)
        .divide(prb).pow(2))

    out = h1.subtract(h2).rename('building_varh').multiply(100).uint16()

  return exportFunc(out, reg, desc)
  #return desc

path = "projects/mmeka-ee/assets/open_buildings_temporal/public_annual_2016_2023"
imcol = (ee.ImageCollection(path)
  .filterDate(year+'-01-01',year+'-12-31'))

ids = imcol.aggregate_array('system:index').distinct().sort()
ids = ids.getInfo()

for idx in tqdm(ids):
  mainFunc(idx)