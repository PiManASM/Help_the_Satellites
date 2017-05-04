from ORM.orm_controller import Controller


class Data:
    # Class handles data obtained from the orm. Gets data and

    def __init__(self):
        self.control = Controller()

    # def data_add(self, data):
    #     self.control.add_data(data)

    def data_query(self, query=None):
        q_data = self.control.query_data(query)
        return q_data

    def math_func(self):
        # we need math!!!
        pass


if __name__ == "__main__":

    # # query DB
    # queryer = Controller()
    # q_data = queryer.query_data('S17181')
    # # for row in data:
    # #     print(data)
    # # q_data.column_descriptions
    # # print(q_data)
    # print(q_data)

    data = Data()
    print(data.data_query('S17181'))
