
#program to calc net_salary from gross_salary

#inputs
emp_gross_salary = 7000

#processing

if emp_gross_salary >= 5000:
    tax = 10
else :
    tax = 0

emp_net_salary = emp_gross_salary - tax / 100 * emp_gross_salary

#outputs
print(emp_net_salary)

