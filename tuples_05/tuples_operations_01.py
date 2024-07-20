print('---- create and print tuple -----')
my_tuple = (101, 'mostafe' , 8000.0, 'giza')
print(my_tuple)
print(type(my_tuple))


print('---------- access element in a tuple by index -------------')
print( my_tuple[3] )


print('------------ un packing tuple ----- ')
emp_code, emp_name, emp_salary, emp_address, = my_tuple
print(emp_code, emp_name, emp_salary ,emp_address)


print('------ Loop over Tuple -------')
for item in my_tuple:
    print(item)





