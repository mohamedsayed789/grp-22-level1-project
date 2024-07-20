
def sum_even_numbers(my_list):
    total_even = 0
    for item in my_list:
        if item % 2 == 0:
            total_even = total_even + item
    return total_even

# main program
# calling function
numbers_list = [5, 6, 10, 3, 20]
total_even_result = sum_even_numbers(numbers_list)
print('total of even numbers in the list = ', total_even_result)
