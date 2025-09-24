import ee
from tqdm import tqdm

'''
Script to process and download building characteristics based on
the Google Open Buildings 2.5D.

See: Priyatikanto et al., A 100-m resolution building characteristics 
for the Global South derived from Google Open Buildings Temporal 
dataset 2016-2023
'''

project_name = input('Enter your project name: ')
band = input('Select band [count, perimeter, surface, volume, distance, varh]: ')
threshold = float(input('Threshold [e.g., 0.5]: '))
year = input('Select year [2016-2023]: ')
print()

ee.Authenticate()
ee.Initialize(project=project_name)

region = ee.Geometry.BBox(-120.000000096,-60.999975942,145.000000014,40.000000176)
crsTransform = [0.00083333333, 0, -179.999999856, 0, -0.00083333333, 84.0]
#crsTransform = [0.00083333333, 0, -120.000000096, 0, -0.00083333333, 40.000000176]

def exportFunc(image, region, desc):
  task = ee.batch.Export.image.toDrive(
    image=image,
    region=region,
    description=desc,
    folder='openBuildings_'+year,
    crs='EPSG:4326',
    crsTransform=crsTransform,
    maxPixels=1e12,
    shardSize=256,
    fileDimensions=65536
  )
  task.start()
  #print(desc)

def mainFunc(band, idx, threshold):
  suffix = f'_t{threshold*10:.0f}_'
  desc = band + suffix + str(idx).replace('-','m')
  img = imcol.filter(ee.Filter.eq('system:index', idx)).first()
  mask = img.select('building_presence').gt(0.4)
  img = img.updateMask(mask)
  reg = img.geometry()

  if (band == 'count'):
    out = (img.select('building_fractional_count')
      .reduceResolution(reducer='sum', maxPixels=1024, bestEffort=True)
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .multiply(4e4).uint16()
      .rename('building_count'))
  elif (band == 'surface'):
    out = (mask.toFloat()
      .reduceResolution(reducer='sum', maxPixels=1024, bestEffort=True)
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .multiply(1e4).uint16()
      .rename('building_surface'))
  elif (band == 'volume'):
    #building volume is in 10 m^3
    out = (hgt.select('building_height')
      .reduceResolution(reducer='sum', maxPixels=1024, bestEffort=True)
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .multiply(1e3).uint16()
      .rename('building_volume'))
  elif (band == 'perimeter'):
    out = (mask.convolve(ee.Kernel.laplacian8(normalize=True)).gt(0)
      .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
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
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
      )
    h1 = (img.select('building_height').pow(2)
      .multiply(fct)
      .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .divide(prb))

    h2 = (img.select('building_height')
      .multiply(fct)
      .reduceResolution(reducer='mean', maxPixels=1024, bestEffort=True)
      #.reproject(crs='EPSG:4326', crsTransform=crsTransform)
      .divide(prb).pow(2))

    out = h1.subtract(h2).rename('building_varh').multiply(100).uint16()

  exportFunc(out, reg, desc)

path = "projects/mmeka-ee/assets/open_buildings_temporal/public_annual_2016_2023"
imcol = (ee.ImageCollection(path)
  .filterDate(year+'-01-01',year+'-12-31'))

ids = imcol.aggregate_array('system:index').distinct().sort()
download_all = input('Do you want to download all available tiles? [Y/N]')
if download_all == 'Y':
  ids = ids.getInfo()
else:
  print('Only download the first tile.')
  ids = ids.getInfo()[0:1]
  
for idx in tqdm(ids):
  mainFunc(band, idx, threshold)

print('Tasks are submitted.')
print('Check https://code.earthengine.google.com/taskts to see the progress')
print('After processing, the extracted raster should be available at'
print('your Google Drive: MyDrive/openBuildings_[year]')