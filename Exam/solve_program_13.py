#Check if an element exists in a list in Python and return all occurrence indexes of the element in this list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 7

is_found = False

for i in range(len(my_list)):
    if number == my_list[i]:
        print('number is found index = ', i)
        is_found = True

if not is_found:
    print('number is not found')
