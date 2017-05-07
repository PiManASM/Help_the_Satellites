"""Map operations to preform on the data"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# lon_0 is the central longitude of the projection.
# resolution = 'l' means use low resolution coastlines.
# optional parameter 'satellite_height' may be used to
# specify height of orbit above earth (default 35,786 km).
m = Basemap(projection='geos',lon_0=18.89,resolution='l')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))
drift =  (18.89+0.002)
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color='aqua')
plt.title("Full Disk Geostationary Projection")
# plt.show()

sat_lon = 18.89
sat_lat = 0
lon = 45.9179
lat = 63.4084
x,y = m(lon, lat)
m.plot(x, y, 'bo', markersize=8)
x,y = m(sat_lon,sat_lat)
m.plot(x, y, 'bo', markersize=8)
x,y = m(drift,0)
m.plot(x,y, ''
            ''
            ''
            'bo',markersize=8)

plt.show()


