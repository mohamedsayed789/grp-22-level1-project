# create 4 functions
"""
1. add_numbers : which add 2 parameters and return result
2. multiply_numbers : which multiply 3 parameters and return result
3. divide_numbers : which divide 2 parameters and return result and check not to divide by Zero
4. abs_numbers : which take 1 parameter : if it is negative just return +ive of this number
"""
def add_numbers(frist_number, second_number):
    return frist_number + second_number

def multiply_numbers(frist_number, second_number, third_number):
    return frist_number * second_number * third_number

def abs_number(value):
    if value < 0:
        return value * (-1)
    else:
        return value

def divide_number(frist_number, second_number):
    if second_number == 0:
        return 'error - cannot divide by zero'
    else:
        return frist_number / second_number

# main program
# calling to all function
add_reslut = add_numbers(7, 8)
multiply_reslut = multiply_numbers(9, 6, 3)
abs_result = abs_number(-20)
divide_result = divide_number(8,2)
print(add_reslut, multiply_reslut, abs_result, divide_result)

