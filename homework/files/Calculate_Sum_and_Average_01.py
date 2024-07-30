# Read File, Store Numbers in a List, and Calculate Sum and Average

new_list = []

with open('C:\\my_files\\read_date_number.txt', 'r') as my_file_reference:
    pen_reader = my_file_reference.readlines()
    print(pen_reader)
    for item in pen_reader:
        item = item.strip()
        new_list.append(int(item))

print(new_list)
total = sum(new_list)
print(total)
average = total / len(new_list)
print(average)
