from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sat_launch.html"), 'html.parser')

string_data = []

for string in soup.stripped_strings:
    string_data.append(string)

print("done")