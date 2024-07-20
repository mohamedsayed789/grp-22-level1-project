#program to read a csv file filter date cy city
import csv

with (open('C:\\my_files\\people.csv', 'r') as my_file_reference1,
      open('C:\\my_files\\people_cairo.csv', 'w',newline='') as my_file_reference2):
    reader_pen = csv.reader(my_file_reference1)
    writer_pen = csv.writer(my_file_reference2)
    writer_pen.writerow(['Name', 'Age', 'City'])
    for row in reader_pen:
       if row[2].lower() == 'cairo'.lower():
           writer_pen.writerow(row)

