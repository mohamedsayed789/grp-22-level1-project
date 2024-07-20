#inputs

first_no = int(input("please enter first no : "))
second_no = int(input("please enter second no : "))
sign = int(input('please enter the sign 1 for +  | 2 for - | 3 for * | 4 for / : '))

# processing
if sign == 1:
    print(first_no + second_no)
elif sign == 2:
    print(first_no - second_no)
elif sign == 3:
    print(first_no * second_no)
elif sign == 4:
    print(first_no / second_no)
else:
    print('invalid input')
