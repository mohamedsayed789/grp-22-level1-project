#program to read from text file and store in a list

new_lines_list = []

with open('C:\\my_files\\countries.txt', 'r') as my_file_reference:
    lines_list = my_file_reference.readlines()  #return list of lines
    print(lines_list)
    for item in lines_list:
        item = item.strip()      #remove whitespace or \n from start or end of string
        if item != '':
            new_lines_list.append(item)

print(new_lines_list)

