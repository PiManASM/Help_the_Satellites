from bs4 import BeautifulSoup
import csv



with open('data/soup.txt') as file:
    soup = BeautifulSoup(file, 'html.parser')


# for node in soup.findAll('font'):
    # node.decode()
    # print(node)
# print(soup.get_text())
session_list = []
for node in soup.findAll(['tr', 'font']):
    session_list.append(node.get_text())
    # print(node.get_text())

# for item in session_list:
#     print(item + '\n done')

session_list_copy = session_list[:]

for item in session_list_copy:
    item_new = session_list[session_list.index(item)].strip()
    if item_new == '':
        session_list.remove(item)

print(session_list)
for item in session_list:
    print(item + '\n done')

print(len(session_list)/4)
# print(index)


output = [] 
row = []
index = 0 

for item in session_list:
	if (item > "Jan. 0") & (item < "Jan. 32") or (item > "Feb. 0") & (item < "Feb. 32") or (item == "Feb. 5") or (item > "March 0") & (item < "March 32")or (item > "April 0") & (item < "April 32")or (item > "May 0") & (item < "May 32")or (item > "June 0") & (item < "June 32")or (item > "July 0") & (item < "July 32")or (item > "Aug. 0") & (item < "Aug. 32")or (item > "Sept. 0") & (item < "Sept. 32")or (item > "Oct. 0") & (item < "Oct. 32")or (item > "Nov. 0") & (item < "Nov. 32")or (item > "Dec. 0") & (item < "Dec. 32"):
		row.append(session_list[index])
		row.append(session_list[index + 1])
		row.append(session_list[index + 3])
		output.append(row)
		row = []

	index = index + 1 

