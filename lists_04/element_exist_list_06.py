#inputs
my_list = [4, 5, 7, 6, 2, 10]
number = 5

is_found = False

for i in range(len(my_list)):
    if number == my_list[i]:
        print('number is found at index = ', i)
        is_found = True # change the flag
        break # close the loop if number is found for performance

# if is_found == false:
if not is_found:
    print('number is not found')




