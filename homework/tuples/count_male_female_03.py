# Count and print no. of Male, no. of Female in the list of Tuples
company_employees = [
(101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
(102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
(103, 'Adham Aly', 5000.0, 'Engineer','M'),
(104, 'Islam Hassan', 7000.0, 'Sales','M'),
(105, 'Mostafa Esam', 7000.0, 'Marketer','M'),
(106, 'Ola Hassan', 7000.0, 'Engineer','S')
]

male_counter, female_counter = 0, 0
for item in company_employees:
    if item[4] == 'M':
        male_counter = male_counter + 1
    elif item[4] == 'F':
        female_counter = female_counter + 1

print('Male count = ', male_counter)
print('Female count = ', female_counter)