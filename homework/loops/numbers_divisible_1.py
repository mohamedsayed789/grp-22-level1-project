# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700

num_list = []
for i in range(1500, 2700 + 1):
    if i % 5 == 0 and i % 7 == 0:
        num_list.append(str(i))  # convert to str list to join

# convert back from list to string
final_statement = ','.join(num_list)
print(final_statement)











