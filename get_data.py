import csv
from ORM.orm import Identification

class Data_Retr:
    def __init__(self):
        pass

    def web(self, file):
        pass

    def file(self, file):
        # read the file
        data_list = []
        with open(file) as csvfile: # 'data/geo.csv'
            data = csv.reader(csvfile, delimiter=',')
            for row in data:
                data_list.append(row)

    def save_data(self, data):
        pass

    def create_obj(self, data):
        # create data objects to be put into the db via the session
        session_instances = []
        for row_new in data:
            new_user = Identification(row_new)
            session_instances.append(new_user)


        pass

if __name__ == '__main__':
    pass
