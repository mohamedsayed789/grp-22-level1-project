# Read File, Store Numbers in a List, and Calculate Sum and Average

new_list = []

with open('C:\\my_files\\read_date_number.txt', 'r') as my_file_reference:
    number_list = my_file_reference.readlines()
    print(number_list)
    for item in number_list:
        item = item.strip()
        new_list.append(item)

print(new_list)
new_list = sum(new_list)
print(new_list)








