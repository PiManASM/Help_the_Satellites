from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import Column, Integer, String


# class creates the connect on instantiation and contains methods for updating data to the database as well as pulling
# data from the database

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:root@localhost/satellite', echo=True)


class Identification(Base):

    __tablename__ = 'identification'

    cospar_desg = Column(String(6), primary_key=True)
    norad_id = Column(String(10))  # primary_key=True)
    name = Column(String(64))
    alt_name = Column(String(64))
    julian_date = Column(String(64))
    gregorian_date = Column(String(64))
    geo_stat = Column(String(64))
    orbital_period = Column(Integer())
    perigee = Column(Integer())
    apogee = Column(Integer())
    inclination = Column(Integer())
    longitude = Column(String(64))
    drift_rate = Column(String(64))


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

    # def add_data(self, add_map):
    #
    #     try:
    #         self.session.add_all(add_map)
    #         self.session.commit()
    #     except InvalidRequestError:
    #         self.session.rollback()
    #         raise
    #     except: #I cannot remember the name of the error, but the one that happens when nothing exist
    #         # call nothing_exist and make stuff
    #         pass

    # the important class
    def query_data(self):  # , query):
        try:
            for satellite in self.session.query(Identification.cospar_desg).\
                    filter_by(norad_id='1986-096A'):
                print(satellite)
        except: # some exception
            pass
        return satellite