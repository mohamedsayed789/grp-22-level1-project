# program to read and print the content of a text file
"""
to read a text files
open the file
read the content
close the file
"""
print('----first way------')
my_file_reference = open("C:\\my_files\\read_date.txt",'r')
content = my_file_reference.read()
print(content)
my_file_reference.close()

print('----second way using with clause ignore close()------')
with open("C:\\my_files\\read_date.txt",'r') as my_file_reference:
    content = my_file_reference.read()
    print(content)
