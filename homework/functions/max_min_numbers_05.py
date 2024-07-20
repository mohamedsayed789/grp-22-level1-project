# Write a function get_max_num() that is used to
#		> return Max no of a List
#	 Write a function get_min_num() that is used to
#		> return Min no of List
def max_number_list(my_list):
    max = my_list[0]
    for item in my_list:
        if item > max:
            max = item
    return max

def min_number_list(my_list):
    min = my_list[0]
    for item in my_list:
        if item < min:
            min = item
    return min

# main program
my_list = [15, 6, 22, 7, 19, 30, 14]
print('Max No. = ', max_number_list(my_list))
print('Min No. = ', min_number_list(my_list))