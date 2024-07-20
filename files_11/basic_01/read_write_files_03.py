# program to read from a file and write the content to anthor file
with open("C:\\my_files\\read_date.txt",'r') as my_file_reference:
    content = my_file_reference.read()

with open("C:\\my_files\\write_data2.txt",'w') as my_file_reference:
    my_file_reference.write(content)
