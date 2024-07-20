# Count occurrence of a number in a list

# input
my_list = [4, 5, 6, 1, 2, 6, 10]
my_num = 6

# processing
counter = 0
for item in my_list:
    if my_num == item:
        counter = counter + 1


# output
print('number occur times = ', counter)
