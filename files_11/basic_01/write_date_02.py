# program to write date to a text files

print('------first way-------')

my_file_reference = open("C:\\my_files\\write_date.txt",'w')
my_file_reference.write('i like programming\n')
my_file_reference.write('i like football\n')
my_file_reference.write('python is my favourite programming language\n')
my_file_reference.close()


print('----second way using with clause ignore close()------')
with open("C:\\my_files\\write_date.txt",'a') as my_file_reference:
    my_file_reference.write('\n')
    my_file_reference.write('my city is cairo\n')
    my_file_reference.write('my city is alex\n')
    my_file_reference.write('iam an engineer')

