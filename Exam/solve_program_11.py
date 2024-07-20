#Solve password validation for rules

str = 'sr@m@_f0rtu9e$._2023'
count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0
if len(str) > 8:
    for letter in str:
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
        print('not valid password')

else:
    print('invalid password - should be > 8 letter')



