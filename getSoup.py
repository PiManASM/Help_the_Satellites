from bs4 import BeautifulSoup

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

