# Find the Max and Min element from a list

my_list = [5, 4, 10, 7, 20]
mix_number = my_list[0]
max_number = my_list[0]


for item in my_list:
    if item < mix_number:
        min_number = item

    if item > max_number:
        max_number = item

print('Min number = ', min_number)
print('Min number = ', min(my_list))
print('Max number = ', max_number)
print('Max number = ', max(my_list))