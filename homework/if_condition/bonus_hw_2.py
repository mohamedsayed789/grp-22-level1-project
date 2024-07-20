#
emp_salary = input("please enter a no : ")
emp_salary = int(emp_salary)

bouns = 0


if emp_salary >= 5000:
    bouns = 2000
    emp_salary = emp_salary + bouns
    # print(emp_salary + bouns)
else:
    bouns = 4000
    emp_salary = emp_salary + bouns
    # print(emp_salary + bouns)

print(emp_salary)



