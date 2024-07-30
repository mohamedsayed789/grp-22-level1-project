# Read File, validate password with valid complexity and write them to another file,
# contains capital, small, numbers, special characters
new_list = []
with open('C:\\my_files\\passwords.txt', 'r') as my_file_refernce:
    pen_reader = my_file_refernce.readlines()
    print(pen_reader)
    for item in pen_reader:
        item = item.strip()
        new_list.append(item)
print(new_list)
count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0
if len(new_list) > 8:
        for letter in new_list:
            if letter.isupper():
                count_upper = count_upper + 1
            elif letter.islower():
                count_lower = count_lower + 1
            elif letter.isdigit():
                count_digits = count_digits + 1
            elif not letter.isalnum():
                count_signs = count_signs + 1
        if count_upper >= 1 and count_lower >= 1 and count_digits >= 1 and count_signs >= 1:
            print('valid password')
        else:
            print('invalid password')
else:
    print('invalid password - should be > 8 letter')

