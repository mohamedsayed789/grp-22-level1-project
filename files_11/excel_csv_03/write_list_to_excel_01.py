#program to write list content to a csv file
import csv

people_list = [
    ['Name', 'Age', 'City'],
    ['adham', 25, 'assuit'],
    ['esam', 30, 'cairo'],
    ['shady', 28 , 'mansoura']
]

with open('C:\\my_files\\people.csv', 'w', newline='') as my_file_reference:
    write_pen = csv.writer(my_file_reference)
    for item in people_list:
        write_pen.writerow(item)

    """
    write_pen.writerow( ['id', 'name', 'salary'] )
    write_pen.writerow( ['101', 'yahia', '7000'] )
    write_pen.writerow( ['102', 'omer', '5000'] )
    write_pen.writerow( ['103', 'hoda', '9000'] )
    """

