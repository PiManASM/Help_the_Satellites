from datetime import datetime

cospar_desg='S32708',
norad_id='2008-011A',
name='AMC 14',
alt_name='Americom 14',
gregorian_date=datetime.strptime('2017 Apr 22 2352 UTC', '%Y %b %d %H%M %Z'),
orbital_period='1436.059',
perigee='35611',
apogee='35960',
inclination='19.02',
longitude='18.89E',
drift_rate='0.002E'


# launch
launch_date=datetime.strptime('March 14 2017 2318 UTC', '%B %d %Y %H%M %Z'),
# site=
rocket_name='Proton'

#site
address='Baikonur Cosmodrome, Кармакшинский район, Kyzylorda Region, Kazakhstan',
latitude='45.9178932',
longitude='63.4083721370363'


from ORM.orm_controller import Controller, Site, Launch, Identification
from datetime import datetime
Identification(cospar_desg='S32708',
norad_id='2008-011A',
name='AMC 14',
alt_name='Americom 14',
gregorian_date=datetime.strptime('2017 Apr 22 2352 UTC', '%Y %b %d %H%M %Z'),
orbital_period='1436.059',
perigee='35611',
apogee='35960',
inclination='19.02',
longitude='18.89E',
drift_rate='0.002E')
list = []
list.append(Identification(cospar_desg='S32708',
norad_id='2008-011A',
name='AMC 14',
alt_name='Americom 14',
gregorian_date=datetime.strptime('2017 Apr 22 2352 UTC', '%Y %b %d %H%M %Z'),
orbital_period='1436.059',
perigee='35611',
apogee='35960',
inclination='19.02',
longitude='18.89E',
drift_rate='0.002E'))
list.append(Launch(launch_date=datetime.strptime('March 14 2017 2318 UTC', '%B %d %Y %H%M %Z'),
rocket_name='Proton'
))
list.append(Site(address='Baikonur Cosmodrome, Кармакшинский район, Kyzylorda Region, Kazakhstan',
latitude='45.9178932',
longitude='63.4083721370363'
))
con = Controller()
con.session.add_all(list)
con.session.commit()



from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# lon_0 is the central longitude of the projection.
# resolution = 'l' means use low resolution coastlines.
# optional parameter 'satellite_height' may be used to
# specify height of orbit above earth (default 35,786 km).
m = Basemap(projection='geos',lon_0=-105,resolution='l')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color='aqua')
plt.title("Full Disk Geostationary Projection")
plt.show()