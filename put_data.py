import csv
from ORM.orm_controller import Identification, Launch
import unicodedata
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import pickle



# add to DB
# new_file = DataRetr()
# sats = new_file.file('data/geo.csv')
# add = Controller()
# add.add_data(sats)
class DataRetr:
    def __init__(self):
        self.iden_list = []
        self.launch_list = []
        self.launch_data = ['date', 'name', 'launch time', 'launch site']
        self.problem_sites = ['Cape Canaveral', 'Kennedy Space Center', 'Vandenberg Air Force Base']
        self.name_list = ['name', 'pre name']


    def get_launch_data(self, in_file):
        temp_data_list = []
        with open(in_file) as open_file:
            for line in open_file:
                if line == '\n':
                    pass
                else:
                    temp_data_list.append(line)
        for row in temp_data_list:
            self.iden_list.append(unicodedata.normalize('NFKD', row).strip())
        # split list from this quick file
        size = 4
        self.iden_list = [self.iden_list[i:i + size] for i in range(0, len(self.iden_list), size)]

        # create temporary list and clear instance list.
        temp_data_list = self.iden_list
        self.iden_list = []
        for row in temp_data_list:
            self.iden_list.append(dict(zip(self.launch_data, row)))
            # print(dict(zip(self.launch_data, row)))
        for row in self.iden_list:
            names_raw = row['name'].split(u"\u2022")
            names = []
            for i in range(0, len(names_raw)):
                names.append(names_raw[i].replace(names_raw[i], names_raw[i].strip()))
            row.update(zip(self.name_list, names))
        for row in self.iden_list:
            row.update({'date': self.process_date_time(row['date'], row['launch time'])})
            if 'launch time' in row:
                del row['launch time']
            row.update({'launch site': self.process_launch_site(row['launch site'])})
        return self.iden_list

    # @staticmethod
    def process_date_time(self, date, date_time):
        # choose month
        full_months = ['March', 'April', 'May', 'June', 'July']
        month = date.split(' ')[0]
        if month.find('.') != -1:
            month = month.replace('.', '')
        # choose with day if two are presented
        index = date.find('/')
        if index != -1:
            options = [date[index-2:index], date[index+1:index+3]]
            for i in options:
                if date_time.find(i + 'th') != -1:
                    day = i
        else:
            day = date.split(' ')[1]
        # motherfucker does not have a date...
        time = date_time.split(':')[1].strip()[0:4]
        time = time[0:2] + ':' + time[2:4]
        if month in full_months:
            datetime_object = datetime.strptime(month + ' ' + day + ' ' + '2017' + ' ' + time + ' UTC', '%B %d %Y %H:%M %Z')
        else:
            datetime_object = datetime.strptime(month + ' ' + day + ' ' + '2017' + ' ' + time + ' UTC', '%b %d %Y %H:%M %Z')
        return datetime_object

    def process_launch_site(self, launch_site):
        # need GeocoderTimedOut error handling
        if launch_site.find('Launch site') != -1:
            launch_site = launch_site.split(':', 1)[1]
        if any(string in launch_site for string in self.problem_sites):
            launch_site = launch_site.split(',', 1)[1].strip()

        locator = Nominatim()
        try:
            location = locator.geocode(launch_site)
        except GeocoderTimedOut:
            try:
                location = locator.geocode(launch_site)
            except GeocoderTimedOut:
                try:
                    location = locator.geocode(launch_site)
                except GeocoderTimedOut:
                    return None
        # print(location)
        return location

    def get_from_web(self, file):
        pass

    def read_sat_file(self, file):
        # read the file
        with open(file) as csvfile: # 'data/geo.csv'
            data = csv.reader(csvfile, delimiter=',')
            # ensure list is empty
            self.iden_list = []
            for row in data:
                self.iden_list.append(row)
        return self.create_Iden_obj()

    def create_Launch_ojj(self, data):
        session_instances = []
        for new_row in data:
            new_user = Launch(launch_site=new_row['launch site'],
                              name=new_row['name'],
                              pre_name=new_row['pre name'],
                              date=new_row['date']
            )
            session_instances.append(new_user)
        return session_instances

    def create_Iden_obj(self):
        # create data objects to be put into the db via the session
        session_instances = []
        for new_row in self.iden_list:
            new_user = Identification(cospar_desg=new_row[0],
                                      norad_id=new_row[1],
                                      name=new_row[2],
                                      alt_name=new_row[3],
                                      julian_date=new_row[4],
                                      gregorian_date=new_row[5],
                                      geo_stat=new_row[6],
                                      orbital_period=new_row[7],
                                      perigee=new_row[8],
                                      apogee=new_row[9],
                                      inclination=new_row[10],
                                      longitude=new_row[11],
                                      drift_rate=new_row[12]
                                      )

            session_instances.append(new_user)
        return session_instances

if __name__ == '__main__':
    from ORM.orm_controller import Controller

    add = DataRetr()
    file = 'data/launches.txt'
    data = add.get_launch_data(file)
    print(data)
    data_instances = add.create_Launch_ojj(data)
    control = Controller()
    control.add_data(data_instances)
    # print('Finished motherfucker')
    # for row in data:
        # print(row['name'])
        # name_list = ['name', 'pre_name']
        # names = row['name'].split(u"\u2022")
        # row.update(zip(name_list,names))
        # print(row)
        # print(row['name'])
        # for letter in name:
        #     pass
