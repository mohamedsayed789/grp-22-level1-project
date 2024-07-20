#program to read from excel file into a list
import csv

new_people_list = []
with open('C:\\my_files\\people.csv', 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)

    for row in reader_pen:
        new_people_list.append(row)

print(new_people_list)
