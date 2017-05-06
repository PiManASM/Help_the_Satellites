# the important method
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
from ORM.orm_controller import Controller, Identification, Launch


class query:

    def __init__(self):
        self.control = Controller()

    def make_query(self, user_query):
        """Compare query to query types and send to function"""
        if user_query == 'name_col':
            return self.name_col()


    def name_col(self):
        satellites = self.control.session.query(Identification.name, Identification.alt_name, Identification.cospar_desg)
        self.ret_list = satellites.all()
        return self.ret_list


if __name__ == '__main__':
    a = query()
    print(a.make_query('name_col'))
