# Novel 100-m Resolution Building Characteristics for the Global South: Insights from the Google Open Buildings Temporal Dataset (2016-2023)

With global populations on the rise, particularly in the Global South, there's an increasing need for high-resolution data on built-up areas. This data is crucial for accurate population modeling, effective urban planning, and insightful environmental research, but existing datasets often lack the necessary detail or coverage.

To address this gap, our study utilized the Google Open Buildings 2.5D Temporal dataset, spanning from 2016 to 2023. We processed this data to derive six key 100-meter resolution building characteristics: building count, total perimeter, total area, total volume, height variance, and mean distance between buildings. These metrics were calculated through a combination of arithmetic operations, convolutions, and spatial aggregation. We rigorously validated our derived data against Google Open Buildings 2.0, Microsoft Building Footprints, GHSL, and WSF3D. We also assessed the dataset's temporal consistency and investigated the effectiveness of polynomial fitting for smoothing temporal fluctuations.

The new dataset exhibited strong correlations with Google 2.0 (e.g., an $r$-value of 0.88 for building count and 0.90 for building area), although we observed a systematic underestimation of perimeters in densely built areas. Correlations with GHSL and WSF3D were weaker, primarily due to inherent methodological differences. An interesting finding was the moderate correlation ($r = 0.47$) between building height variance and total volume. Critically, we identified a strong positive correlation ($r > 0.8$) between building count, area, volume, and population. Our temporal analysis revealed significant fluctuations across most characteristics, especially those related to height, with second-order polynomial fitting proving to be the most effective method for smoothing these variations.

In conclusion, we have successfully developed and validated a valuable 100-meter resolution dataset detailing building characteristics across the Global South, derived from Google Open Buildings 2.5D. While the dataset demonstrates consistency with similar existing resources, its observed temporal fluctuations indicate that further processing is required for applications demanding precise time-series analysis. This new dataset nonetheless offers considerable potential for advancing research in areas such as population distribution modeling, urban planning, and environmental studies.

## Country summary
There are 131 countries covered by the Google Open Buildings 2.5D dataset. The following table summarizes the building characteristics at country-level. All values are in millions.

| TLC   | Country                          | Total Count | Total Perimeter | Total Surface | Total Volume |
|:------|:---------------------------------|------------:|----------------:|--------------:|-------------:|
| ABW   | Aruba                            |       456.8 |             3.2 |          14.2 |          6.4 |
| AGO   | Angola                           |      1565.3 |           214.4 |         588.8 |        274.9 |
| AIA   | Anguilla                         |      2799.7 |             0.7 |           2.3 |          1.2 |
| ARG   | Argentina                        |      3856.6 |           834.9 |         498.7 |       2051.6 |
| ATG   | Antigua and Barbuda              |      2666.0 |             2.8 |           9.0 |          3.9 |
| BDI   | Burundi                          |      3034.2 |            88.8 |         182.8 |         81.8 |
| BEN   | Benin                            |      1225.8 |           132.1 |         378.7 |        166.5 |
| BES   | Bonaire, Sint Eustatius and Saba |      3287.9 |             1.0 |           3.7 |          1.7 |
| BFA   | Burkina Faso                     |      3062.7 |           211.1 |         359.8 |        135.4 |
| BGD   | Bangladesh                       |       991.5 |          1041.5 |        1527.8 |       1314.1 |
| BHS   | Bahamas                          |      4030.8 |             9.9 |          38.2 |         18.2 |
| BLM   | Saint Barthelemy                 |       199.0 |             0.3 |           0.9 |          0.4 |
| BLZ   | Belize                           |      1948.2 |             9.1 |          27.4 |         11.4 |
| BOL   | Bolivia                          |      3121.4 |           183.7 |         673.6 |        349.5 |
| BRA   | Brazil                           |      2686.7 |           751.8 |         361.3 |       1510.6 |
| BRB   | Barbados                         |       670.8 |             7.6 |          28.6 |         12.9 |
| BRN   | Brunei                           |      3997.8 |             9.6 |          50.9 |         36.5 |
| BTN   | Bhutan                           |      1514.3 |            14.8 |          41.2 |         26.5 |
| BWA   | Botswana                         |      1380.3 |            63.2 |         149.6 |         62.1 |
| CAF   | Central African Republic         |      1930.6 |            35.4 |          60.4 |         23.4 |
| CHL   | Chile                            |      1136.5 |           355.0 |        1576.9 |        902.3 |
| CHN   | China                            |      4222.2 |           202.1 |         921.4 |        634.7 |
| CIV   | CIte dIvoire                     |      1681.7 |           236.3 |         705.9 |        311.8 |
| CMR   | Cameroon                         |      4225.9 |           232.3 |         713.3 |        358.8 |
| COD   | Democratic Republic of the Congo |      1743.4 |           480.7 |         911.2 |        367.1 |
| COG   | Republic of Congo                |       720.2 |            40.7 |         137.0 |         71.8 |
| COL   | Colombia                         |      3807.6 |           469.4 |        2146.2 |       1295.4 |
| COM   | Comoros                          |       407.3 |             6.0 |          24.3 |         12.0 |
| CPV   | Cape Verde                       |      1273.5 |             6.4 |          24.3 |         15.1 |
| CRI   | Costa Rica                       |      2085.0 |            84.1 |         376.7 |        188.1 |
| CUB   | Cuba                             |       463.2 |           141.5 |         529.1 |        229.6 |
| CUW   | Curacao                          |      2649.4 |             5.4 |          22.1 |          9.8 |
| CYM   | Cayman Islands                   |      2082.8 |             1.9 |           7.7 |          4.0 |
| DJI   | Djibouti                         |      4254.0 |             3.4 |          15.7 |          9.0 |
| DMA   | Dominica                         |      1257.8 |             1.7 |           5.2 |          2.8 |
| DOM   | Dominican Republic               |       698.8 |           116.2 |         455.8 |        210.6 |
| DZA   | Algeria                          |      3179.7 |           540.5 |        1720.8 |       1634.4 |
| ECU   | Ecuador                          |       326.6 |           226.2 |         969.0 |        529.3 |
| EGY   | Egypt                            |      3513.8 |           556.7 |         853.0 |       1312.6 |
| ERI   | Eritrea                          |      4064.6 |            22.6 |          48.6 |         22.9 |
| ESP   | Spain                            |       311.6 |            48.3 |         270.9 |        192.6 |
| ETH   | Ethiopia                         |       795.5 |           933.9 |        2119.4 |        938.2 |
| FLK   | Falkland Islands                 |      1755.9 |             0.4 |           1.4 |          0.8 |
| GAB   | Gabon                            |      3711.2 |            26.1 |         101.1 |         54.6 |
| GHA   | Ghana                            |      3879.6 |           346.7 |        1202.3 |        589.0 |
| GIB   | Gibraltar                        |        12.1 |             0.2 |           1.5 |          2.1 |
| GIN   | Guinea                           |      4221.5 |           120.4 |         331.7 |        151.0 |
| GLP   | Guadeloupe                       |      2298.8 |            14.0 |          51.2 |         23.8 |
| GMB   | Gambia                           |      3034.2 |            19.3 |          67.7 |         33.0 |
| GNB   | Guinea-Bissau                    |      2710.8 |            16.8 |          60.5 |         29.8 |
| GNQ   | Equatorial Guinea                |      1086.5 |            11.5 |          46.4 |         24.6 |
| GRD   | Grenada                          |      2842.6 |             3.0 |           8.7 |          4.9 |
| GTM   | Guatemala                        |      2018.2 |           221.4 |         813.0 |        380.1 |
| GUF   | French Guiana                    |      3724.1 |             5.7 |          23.6 |         11.7 |
| GUY   | Guyana                           |       350.2 |            16.3 |          58.7 |         27.4 |
| HND   | Honduras                         |       717.9 |           131.7 |         438.0 |        199.4 |
| HTI   | Haiti                            |      2905.7 |            89.4 |         233.8 |         89.8 |
| IDN   | Indonesia                        |      3963.3 |          1442.4 |        2031.0 |        673.2 |
| IND   | India                            |        16.9 |          1623.9 |         274.8 |        455.3 |
| IOT   | British Indian Ocean Territory   |      1179.1 |             0.1 |           0.4 |          0.3 |
| ITA   | Italy                            |       602.1 |             0.8 |           2.3 |          1.0 |
| JAM   | Jamaica                          |      2797.8 |            52.5 |         159.0 |         71.3 |
| KEN   | Kenya                            |      3688.2 |           629.3 |        1434.3 |        668.3 |
| KHM   | Cambodia                         |       548.9 |           230.1 |         834.8 |        483.7 |
| KNA   | Saint Kitts and Nevis            |      1290.9 |             1.7 |           5.8 |          2.5 |
| LAO   | Laos                             |      1302.0 |           137.3 |         449.1 |        241.3 |
| LBR   | Liberia                          |      1226.8 |            38.6 |         115.5 |         48.9 |
| LBY   | Libya                            |      3117.7 |             0.0 |           0.0 |          0.0 |
| LCA   | Saint Lucia                      |       931.2 |             4.0 |          12.6 |          6.4 |
| LKA   | Sri Lanka                        |       166.3 |           370.1 |        1139.5 |        625.1 |
| LSO   | Lesotho                          |      3935.1 |            37.0 |          75.9 |         27.4 |
| MAF   | Saint Martin (French part)       |       165.8 |             0.7 |           2.7 |          1.4 |
| MDG   | Madagascar                       |       861.9 |           181.7 |         382.6 |        163.5 |
| MDV   | Maldives                         |       195.0 |             3.7 |          17.5 |         10.5 |
| MEX   | Mexico                           |       233.3 |          1973.5 |         567.5 |         40.5 |
| MLI   | Mali                             |      1663.8 |           180.4 |         395.6 |        166.8 |
| MMR   | Myanmar                          |       680.2 |             0.0 |           0.0 |          0.0 |
| MOZ   | Mozambique                       |      4054.8 |           352.7 |         587.9 |        212.1 |
| MRT   | Mauritania                       |      3765.8 |            42.7 |         101.1 |         44.1 |
| MSR   | Montserrat                       |       175.8 |             0.3 |           0.8 |          0.4 |
| MTQ   | Martinique                       |      2271.6 |            10.7 |          39.3 |         21.9 |
| MUS   | Mauritius                        |      2689.8 |            18.6 |          86.9 |         47.4 |
| MWI   | Malawi                           |      4244.7 |           171.6 |         311.7 |        124.8 |
| MYS   | Malaysia                         |      1281.9 |           430.9 |        1713.6 |       1840.2 |
| MYT   | Mayotte                          |      1266.2 |             2.6 |          10.4 |          5.8 |
| NAM   | Namibia                          |      1085.1 |            55.3 |         138.8 |         62.4 |
| NER   | Niger                            |       430.8 |            83.8 |         142.5 |         55.4 |
| NGA   | Nigeria                          |      2520.7 |          1370.6 |         674.2 |       1845.8 |
| NIC   | Nicaragua                        |      1772.1 |            87.4 |         277.9 |        118.2 |
| NPL   | Nepal                            |      3823.4 |           348.9 |         909.0 |        439.2 |
| PAK   | Pakistan                         |      2701.9 |          1540.4 |        1881.6 |       1195.3 |
| PAN   | Panama                           |      1254.9 |            67.8 |         285.7 |        148.1 |
| PER   | Peru                             |      2566.1 |           416.5 |        1700.0 |        999.1 |
| PHL   | Philippines                      |      2101.0 |           838.2 |        1172.0 |       1676.5 |
| PRI   | Puerto Rico                      |      2364.4 |            85.3 |         358.0 |        169.1 |
| PRT   | Portugal                         |       183.8 |             7.1 |          24.5 |         16.6 |
| PRY   | Paraguay                         |      1499.8 |           134.8 |         452.4 |        222.0 |
| REU   | Reunion                          |      3588.8 |            20.6 |          80.5 |         48.3 |
| RWA   | Rwanda                           |      1378.6 |           144.0 |         329.8 |        149.5 |
| SDN   | Sudan                            |      3789.9 |           329.4 |         745.2 |        335.1 |
| SEN   | Senegal                          |      4255.7 |           112.8 |         356.7 |        184.2 |
| SGP   | Singapore                        |      1514.4 |            14.2 |         111.5 |        216.1 |
| SHN   | Saint Helena                     |      3129.4 |             0.4 |           1.2 |          0.7 |
| SLE   | Sierra Leone                     |      2016.2 |            45.5 |         144.5 |         63.6 |
| SLV   | El Salvador                      |      3060.2 |            85.0 |         322.2 |        155.1 |
| SOM   | Somalia                          |      2761.0 |            53.8 |         164.2 |         73.1 |
| SSD   | South Sudan                      |      3752.8 |            48.4 |          67.8 |         24.6 |
| STP   | Sao Tome and Principe            |       428.7 |             2.6 |           7.7 |          3.7 |
| SUR   | Suriname                         |      3916.2 |            14.7 |          65.1 |         33.7 |
| SWZ   | Swaziland                        |      4293.7 |            28.7 |          63.7 |         25.5 |
| SXM   | Sint Maarten (Dutch part)        |        73.9 |             0.9 |           3.8 |          2.2 |
| SYC   | Seychelles                       |      3364.3 |             2.4 |           9.1 |          6.3 |
| TCA   | Turks and Caicos Islands         |      1120.1 |             1.2 |           4.3 |          2.2 |
| TCD   | Chad                             |      1458.1 |            95.8 |         146.0 |         53.3 |
| TGO   | Togo                             |      2174.8 |            82.2 |         227.6 |         94.4 |
| THA   | Thailand                         |      2230.6 |          1535.9 |        1503.7 |          9.8 |
| TLS   | East Timor                       |      1572.9 |            16.8 |          45.2 |         19.4 |
| TTO   | Trinidad and Tobago              |      1978.0 |            29.1 |         135.1 |         68.3 |
| TUN   | Tunisia                          |       821.0 |           230.7 |        1033.4 |        549.9 |
| TZA   | Tanzania                         |      1179.3 |           617.6 |        1330.7 |        579.2 |
| UGA   | Uganda                           |      1873.0 |           389.9 |         825.6 |        367.2 |
| URY   | Uruguay                          |      1761.8 |            81.8 |         334.7 |        171.2 |
| VCT   | Saint Vincent and the Grenadines |      3681.8 |             2.7 |           8.5 |          4.6 |
| VEN   | Venezuela                        |      1768.9 |           369.1 |        1604.3 |        835.8 |
| VGB   | British Virgin Islands           |      3257.6 |             0.8 |           2.7 |          1.5 |
| VIR   | Virgin_Islands_U_S               |       494.1 |             3.7 |          13.4 |          7.3 |
| VNM   | Vietnam                          |       181.1 |          1467.5 |        1987.5 |        279.0 |
| ZAF   | South Africa                     |      3783.0 |          1134.3 |         458.0 |       1848.9 |
| ZMB   | Zambia                           |      1191.9 |           190.0 |         414.1 |        172.9 |
| ZWE   | Zimbabwe                         |      2218.1 |           231.1 |         456.8 |        180.6 |

## Processing scripts
- `openBuildings_download.py`: equipped with Python `ee` package, this script can be used to compute 6 building characteristics and aggregate the data to 100-m resolution raster.