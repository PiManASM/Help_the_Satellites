with open('data/sat_launch.html') as file:
    list = []
    for line in file:
        if line.find('<TD') == -1 and line.find('<IMG') == - 1 and line.find('</TR') == -1 and line.find('<TABLE') == -1:
            list.append(line)

with open('data/new_test.txt', 'w') as file:
    for line in list:
        file.write(line)

