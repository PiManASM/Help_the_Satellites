# import csv
from ORM.orm_controller import Controller, Identification


# class DataRetr:
#     def __init__(self):
#         self.data_list = []
#
#     def web(self, file):
#         pass
#
#     def file(self, file):
#         # read the file
#         with open(file) as csvfile: # 'data/geo.csv'
#             data = csv.reader(csvfile, delimiter=',')
#             for row in data:
#                 self.data_list.append(row)
#         return self.create_obj()
#
#     def save_data(self, data):
#         pass
#
#     def create_obj(self):
#         # create data objects to be put into the db via the session
#         session_instances = []
#         for new_row in self.data_list:
#             new_user = Identification(cospar_desg=new_row[0],
#                                       norad_id=new_row[1],
#                                       name=new_row[2],
#                                       alt_name=new_row[3],
#                                       julian_date=new_row[4],
#                                       gregorian_date=new_row[5],
#                                       geo_stat=new_row[6],
#                                       orbital_period=new_row[7],
#                                       perigee=new_row[8],
#                                       apogee=new_row[9],
#                                       inclination=new_row[10],
#                                       longitude=new_row[11],
#                                       drift_rate=new_row[12]
#                                       )
#
#             session_instances.append(new_user)
#         return session_instances


class Data:
    def __init__(self):
        self.control = Controller()

    # def data_add(self, data):
    #     self.control.add_data(data)

    def data_query(self, query):
        pass


if __name__ == "__main__":
    # add to DB
    # new_file = DataRetr()
    # sats = new_file.file('data/geo.csv')
    # add = Controller()
    # add.add_data(sats)

    # query DB
    query = Controller()
    data = query.query_data()
    print(type(data))
    print(data[0])
