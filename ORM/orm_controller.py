from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError

# class creates the connect on instantiation and contains methods for updating data to the database as well as pulling
# data from the database
class Controller:

    engine = create_engine('mysql+mysqlconnector://root:root@localhost/satellite', echo=True)

    Base = declarative_base()

    session_create = sessionmaker()
    session_create.configure(bind=Base)
    session = session_create()

    def nothing_exist(self):
        # use the meta data to create tables.
        # this should probably raise an error. It will indicate some messed up stuff
        pass

    def update_data(self):
        pass

    def add_data(self, add_map):
        try:
            self.session.addall(add_map)
            self.session.commit()
        except InvalidRequestError:
            self.session.roll_back()
            raise
