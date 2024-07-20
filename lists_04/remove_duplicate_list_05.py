#inputs
my_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

#operation
unique_list = []
duplicate_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicate_list:
        duplicate_list.append(item)

#outputs
print('unique list = ', unique_list)
print('duplicate list = ', duplicate_list)
