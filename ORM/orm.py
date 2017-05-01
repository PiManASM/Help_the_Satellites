from sqlalchemy import Column, Integer, String
from ORM.orm_controller import Controller


class Identification(Controller.Base):

    __tablename__ = 'identification'

    cospar_desg = Column(String(6), primary_key=True)
    norad_id = Column(String(10)) # primary_key=True)
    name = Column(String(64))
    alt_name = Column(String(64))
    julian_date = Column(String(64))
    gregorian_date = Column(String(64))
    geo_stat = Column(String(64))
    orbital_period = Column(Integer(20))
    perigee = Column(Integer(20))
    apogee = Column(Integer(20))
    inclination = Column(Integer(20))
    longitude = Column(String(64))
    drift_rate = Column(String(64))

    def __init__(self, row):
        self.cospar_desg = row[0],
        self.norad_id = row[1],
        self.name = row[2],
        self.alt_name = row[3],
        self.julian_date = row[4],
        self.gregorian_date = row[5],
        self.geo_stat = row[6],
        self.orbital_period = row[7],
        self.perigee = row[8],
        self.apogee = row[9],
        self.inclination = row[10],
        self.longitude = row[11],
        self.drift_rate = row[12]
