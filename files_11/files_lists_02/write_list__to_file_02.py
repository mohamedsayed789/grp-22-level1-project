#program to write element of a list into a text file

cities_list = ['cairo','alex', 'mansoura', 'sharqia', 'luxor', 'sohag', 'aswan']

with open('C:\\my_files\\cities.txt', 'w') as my_file_reference:
    for i in range(len(cities_list)):
        if i == len(cities_list) - 1: # the last loop
            my_file_reference.write(cities_list[i])
        else:
            my_file_reference.write(cities_list[i] + '\n')
