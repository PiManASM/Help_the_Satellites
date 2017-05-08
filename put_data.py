import csv
from ORM.orm_controller import Identification, Launch
import unicodedata
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

"""
BaseClass handles creating universal variables, initializing the SQL controller, and errors.
Child class satellites and launches handle the specific files, data types, and initializing the SQLAlchemy classes 
defined in ORM.orm_controller.
"""


class BaseClass:
    """Class that will be inherited by the table specific tables"""

    def __init__(self):
        self.data_list = []
        self.session_instances = []
        self.control = Controller()
        print('initialized')
        pass

    def _addtodb(self):
        # add exceptional handling
        control = Controller()
        control.add_data(data)


    def errors(self):
        """Determines what happened in the case of errors"""
        pass


class satellites(BaseClass):
    """Uses a generated CSV file to populate the DB"""
    def putindb(self, file):
        """Takes prepared CSV file and puts it in the data base"""
        # Add error handling
        self._getdata(file)
        self._createobjects()
        self._addtodb()

    def _getdata(self, file):
        with open(file) as open_file:
            file_lines = csv.reader(open_file, delimiter=',')
        for row in file_lines:
            self.data_list.append(row)

    def _createobjects(self):
        for new_row in self.data_list:
            new_user = Identification(cospar_desg=new_row[0],
                                      norad_id=new_row[1],
                                      name=new_row[2],
                                      alt_name=new_row[3],
                                      gregorian_date=new_row[5],
                                      orbital_period=new_row[7],
                                      perigee=new_row[8],
                                      apogee=new_row[9],
                                      inclination=new_row[10],
                                      longitude=new_row[11],
                                      drift_rate=new_row[12],
                                      launch=[]
                                      )
            self.session_instances.append(new_user)


class launchsite(BaseClass):

    def __init__(self):
        self.problem_sites = ['Cape Canaveral', 'Kennedy Space Center', 'Vandenberg Air Force Base']

    def process_launch_site(self, launch_site):
        # need GeocoderTimedOut error handling
        if launch_site.find('Launch site') != -1:
            launch_site = launch_site.split(':', 1)[1]
        if any(string in launch_site for string in self.problem_sites):
            launch_site = launch_site.split(',', 1)[1].strip()

        locator = Nominatim()
        try:
            location = locator.geocode(launch_site, language='en')
        except GeocoderTimedOut:
            try:
                location = locator.geocode(launch_site, language='en')
            except GeocoderTimedOut:
                try:
                    location = locator.geocode(launch_site, language='en')
                except GeocoderTimedOut:
                    return None
        # print(location)
        location_dict = {'address': location.address, 'latitude': location.latitude, 'longitude': location.latitude}
        return location_dict


class launches(BaseClass):
    """Will use BS4 data to populate the DB"""
    def __init__(self):
        pass

    def get_from_web(self, file):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(open('data/sat_launch.html'), 'html.parser')

        string_data = []

        for string in soup.stripped_strings:
            string_data.append(string)
        return string_data

    # def read_sat_file(self, file):
    #     # read the file
    #     with open(file) as csvfile: # 'data/geo.csv'
    #         data = csv.reader(csvfile, delimiter=',')
    #         # ensure list is empty
    #         self.iden_list = []
    #         for row in data:
    #             self.iden_list.append(row)
    #     return self.create_Iden_obj()

    def get_launch_data(self, in_file):
        temp_data_list = []
        # with open(in_file) as open_file:
        #     for line in open_file:
        #         if line == '\n':
        #             pass
        #         else:
        #             temp_data_list.append(line)
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

        # name processes; add to method and deal with multiple satellites on rocket
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
    # def do_things(self):
    #     self.name_list = control.query_data('name_col')
    #     result = '0'
    #     data_instances_copy = list(data_instances)
    #     for satellite_list in data_instances_copy:
    #         for item in self.name_list:
    #             if satellite_list.satellite_name in item:
    #                 result = '1'
    #                 break
    #         if result == '0':
    #             data_instances.remove(satellite_list)
    #
    #     control.add_data(data_instances)

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
        self.name_list = ['rocket name', 'satellite name']


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

        # name processes; add to method and deal with multiple satellites on rocket
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
            datetime_object = datetime.strptime(month + ' ' + day + ' ' + '2017' + ' ' + time + ' UTC',
                                                '%B %d %Y %H:%M %Z')
        else:
            datetime_object = datetime.strptime(month + ' ' + day + ' ' + '2017' + ' ' + time + ' UTC',
                                                '%b %d %Y %H:%M %Z')
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
        # location = pickle.dumps(location)
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
                              rocket_name=new_row['rocket name'],
                              satellite_name=new_row['satellite name'],
                              date=new_row['date'],
                              # to be implemented
                              cospar_desg=None
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
                                      # may need only one date
                                      julian_date=new_row[4],
                                      gregorian_date=new_row[5],
                                      # to be removed
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

    # add geo data to DB
    # add = DataRetr()
    # file = 'data/geo.csv'
    # data = add.read_sat_file(file)
    # print(data)
    # control = Controller()
    # control.add_data(data)

    # add launch data to DB
    # add = DataRetr()
    # file = 'data/launches.txt'
    # data = add.get_launch_data(file)
    #
    # data_instances = add.create_Launch_ojj(data)
    # control = Controller()
    #
    # # make sure that only geo satellites are added to the DB; to go to a method
    # name_list = control.query_data('name_col')
    # result = '0'
    # data_instances_copy = list(data_instances)
    # for satellite_list in data_instances_copy:
    #     for item in name_list:
    #         if satellite_list.satellite_name in item[0:2]:
    #             result = '1'
    #             break
    #     if result == '0':
    #         data_instances.remove(satellite_list)
    #
    # control.add_data(data_instances)

    # split names; implemented in the DataRetr class
    # for row in data:
        # print(row['name'])
        # name_list = ['name', 'pre_name']
        # names = row['name'].split(u"\u2022")
        # row.update(zip(name_list,names))
        # print(row)
        # print(row['name'])
        # for letter in name:
        #     pass

    l = launches()
    a = l.get_from_web('')
    month_list = ['January', 'Jan', 'February', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August',
                  'Aug', 'September', 'Sep', 'October', 'Oct', 'November', 'Nov', 'December', 'Dec']
    previous_row = next_row = ''
    session_list = []
    new_list = ['date', 'name', 'time', 'location']
    last_row_was_date = False
    for row in a:
        # make decisions
        # print(row)
        # create index for current row; this may be slow. Probably a better way, but it'll do for now
        current_index = a.index(row)
        previous_row = a[current_index - 1]
        if current_index != len(a) - 1:
            next_row = a[current_index + 1]

        if last_row_was_date:
            new_list.append(unicodedata.normalize('NFKD', row).strip())
            last_row_was_date = False
            continue

        last_row_was_date = False
        # next should be name

        # more if conditions to check for the data we do not want; brackets and such
        if any(x in row for x in month_list):
            # print(row)
            found = row.find('[')
            foundl = len(new_list)
            if row.find('[') == - 1 and len(row) < 20:
                # if len(new_list) < 4:
                #     print('bp')
                new_list = []
                session_list.append(new_list)
                new_list.append(unicodedata.normalize('NFKD', row).strip())
                last_row_was_date = True
                # print(row)
                continue

        if previous_row == 'Launch':

        if previous_row == 'Launch site:':
            # print('next is launch site:')
            new_list.append(unicodedata.normalize('NFKD', row).strip())
            continue
        if previous_row == 'Launch time:':
            # print('next one is important')
            new_list.append(unicodedata.normalize('NFKD', row).strip())
            continue
        if previous_row == 'Launch window:' or previous_row == 'Launch time:' or previous_row == 'Launch\nwindow:':
            new_list.append(unicodedata.normalize('NFKD', row).strip())
            continue

    count = 0
    for list in session_list:
        count += 1
        if len(list) < 4:
            print(list)
            print(session_list.index(list))
            print(a.index(list[0]))

    print(count)
    # print(a[2360:2380])
    #251
    #2382
    print('d')