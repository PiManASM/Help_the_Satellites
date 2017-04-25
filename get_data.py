from bs4 import BeautifulSoup

class Data_Retr:
    def __init__(self):
        pass

    def web(self, file):
        pass

    def file(self, file):
        # read the file
        with open(file, 'r') as data:

            # parsing
            for line in data:
                line.strip()
                data_line = list(filter(lambda a: a != '', line))



if __name__ == '__main__':
    pass
