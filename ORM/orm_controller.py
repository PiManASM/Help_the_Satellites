from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, BigInteger, ForeignKey


# class creates the connect on instantiation and contains methods for updating data to the database as well as pulling
# data from the database

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:root@localhost/satellite', echo=True)


class Launch(Base):

    __tablename__ = 'launches'

    # rename to launch_id
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # to be implemented; foreign key relationship with the identification table
    cospar_desg = Column(String(6), ForeignKey('identification.cospar_desg'))
    date = Column(DateTime(64))
    # to be re-tabled for normalization; launch-site table with site information
    launch_site = Column(LargeBinary(2048))
    rocket_name = Column(String(64))
    # to be removed for normalization
    satellite_name = Column(String(64))

    identification = relationship('Identification', back_populates='launches')

class Identification(Base):

    __tablename__ = 'identification'

    cospar_desg = Column(String(6), primary_key=True)
    norad_id = Column(String(10))  # primary_key=True)
    name = Column(String(64))
    alt_name = Column(String(64))
    # may take out one date
    julian_date = Column(String(64))
    gregorian_date = Column(String(64))
    # to be removed
    geo_stat = Column(String(64))
    orbital_period = Column(Integer())
    perigee = Column(Integer())
    apogee = Column(Integer())
    inclination = Column(Integer())
    longitude = Column(String(64))
    drift_rate = Column(String(64))

    launches = relationship('Launch', back_populates='identification')

    def get_data(self):
        data = {}
        data.update({'cospar_desg': self.cospar_desg})
        data.update({'norad_id': self.norad_id})
        data.update({'name': self.name})
        data.update({'alt_name': self.alt_name})
        data.update({'julian_date': self.julian_date})
        data.update({'gregorian_date': self.gregorian_date})
        data.update({'geo_stat': self.geo_stat})
        data.update({'orbital_periond': self.orbital_period})
        data.update({'perigee': self.perigee})
        data.update({'apogee': self.apogee})
        data.update({'inclination': self.inclination})
        data.update({'longitude': self.longitude})
        data.update({'drift_rate': self.drift_rate})

        return data

    def get_name_col(self):
        data = []
        data.append(self.name)
        data.append(self.alt_name)

        return data

class Controller:

    session_create = sessionmaker()
    session_create.configure(bind=engine)
    session = session_create()

    # def nothing_exist(self):
    #     # use the meta data to create tables.
    #     # this should probably raise an error. It will indicate some messed up stuff
    #     pass

    # def update_data(self):
    #     pass

    def add_data(self, add_map):

        try:
            self.session.add_all(add_map)
            self.session.commit()
        except InvalidRequestError:
            self.session.rollback()
            raise
        except: #I cannot remember the name of the error, but the one that happens when nothing exist
            # call nothing_exist and make stuff
            pass

    # will be replaced with queries.py
    def query_data(self, query):
        """Query types will be defined by a string"""
        if query == 'name_col':
            satellites = self.session.query(Identification.name, Identification.alt_name)
            data = satellites.all()
            return data
        # try:
        # for satellite in self.session.query(Identification).\
        #         filter_by(cospar_desg=query):
        #     print(satellite)
        else:
            satellite = self.session.query(Identification). \
                filter_by(cospar_desg=query)

            # except: # some exception
            #     pass
            data = satellite.all()
            for row in data:
                ret_list = row.get_data()
                # data = data[0].get_data()
                # for row in data[0]:
                # print(row)
            return ret_list