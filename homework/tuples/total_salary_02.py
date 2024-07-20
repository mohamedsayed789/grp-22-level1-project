# Print Sum of salary of all employees – from tuples in a list

company_employees = [
(101, 'Ahmed Esam', 10000.0, 'Cairo'),
(102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
(103, 'Adham Aly', 5000.0, 'Cairo'),
(104, 'Islam Hassan', 7000.0, 'Cairo')
]

total_salary = 0
for item in company_employees:
    total_salary = total_salary + item[2]

print('Total salary = ', total_salary)
