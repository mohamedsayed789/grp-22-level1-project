#  Write a function sum_positive_numbers() that is used to
# return sum of Positive Numbers of a List
# Write a function count_positive_numbers() that is used
# return count of Positive Numbers of a List
def sum_positive_numbers(my_list):
    sum_pos = 0
    for num in my_list:
        if num > 0:
            sum_pos = sum_pos + num
    return sum_pos

def count_positive_numbers(my_list):
    count_pos = 0
    for num in my_list:
        if num > 0:
            count_pos = count_pos + 1
    return count_pos


# main program
my_list = [15, -6, -22, 7, -19, 30]
print('Sum pos = ', sum_positive_numbers(my_list))
print('Count pos = ', count_positive_numbers(my_list))
