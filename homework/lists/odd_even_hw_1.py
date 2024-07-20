# get to sum, count of even numbers, odd numbers from a list
my_list = [15, 16, 20, 3, 9, 20]

total_even_numbers, total_odd_numbers, count_even_numbers, count_odd_nubers = 0, 0, 0, 0

for item in my_list:
    if item % 2 == 0:
        total_even_numbers = total_even_numbers + item
        count_even_numbers = count_even_numbers + 1
    else:
        total_odd_numbers = total_odd_numbers + item
        count_odd_nubers = count_odd_nubers + 1

print('total even numbers =' , total_even_numbers, 'count even numbers =', count_even_numbers)
print('total odd numbers =' , total_odd_numbers, 'count odd numbers =', count_odd_nubers)








