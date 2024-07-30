# Read a CSV file and calculate the average value from a specific column.
import csv
people_list = [
    ['Name', 'Age', 'City'],
    ['adham', 25, 'assuit'],
    ['esam', 30, 'cairo'],
    ['shady', 28 , 'mansoura']
]
new_people_list = []
with open('C:\\my_files\\people.csv', 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    for row in reader_pen:
        new_people_list.append(row)

print(new_people_list)
age = people_list[1][1] + people_list[2][1] + people_list[3][1]
average_age = age / len(people_list)
print(average_age)



