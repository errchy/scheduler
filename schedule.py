#!/usr/bin/python

employees = []

for line in open("1.dat", 'r'):
    item = line.rstrip()
    try:
        if (item[0] == '-'):
            temp = []
            for c in item:
                temp.append(c)
            del temp[0]
            name = ''.join(temp)
            employees.append(name)
        elif (item[0] == 'T'):
            temp = []
            for c in item:
                temp.append(c)
            del temp[0]
            del temp[0]
            del temp[0]
            temp.remove(',')
            print temp
    except IndexError:
        pass
print employees


# Read in employees and availability

# --


Tue = [3, 4, 5, 6, 7, 8]
Wed = [3, 4, 5, 6, 7, 8]
Thu = [3, 4, 5, 6, 7, 8]
Fri = [3, 4, 5, 6, 7, 8]
Sat = [11, 12, 1, 2]

avail = [Tue, Wed, Thu, Fri, Sat]


days = [Tue, Wed, Thu, Fri, Sat]
