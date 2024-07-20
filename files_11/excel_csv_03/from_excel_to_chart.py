#program to read excel file csv and plot a chart
import csv
import matplotlib.pyplot as plt

with open('C:\\my_files\\people.csv', 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    reader_pen.__next__() # skip the first row [header]
    x_axis = [] #name
    y_axis = [] #age
    for row in reader_pen:
        x_axis.append(row[0]) #names
        y_axis.append(float(row[1])) #ages

    plt.bar(x_axis, y_axis)
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Bar chart from csv date')
    plt.xticks(rotation=45)
    plt.show()

