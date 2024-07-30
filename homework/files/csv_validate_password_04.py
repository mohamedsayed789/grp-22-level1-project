# Read csv, validate password with valid complexity and write them to another csv file,
# contains capital, small, numbers, special
import csv

new_people_list = []
with open('C:\\my_files\\read_date_number.csv', 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    for row in reader_pen:
        new_people_list.append(row)

print(new_people_list)

