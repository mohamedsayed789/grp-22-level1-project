persons_list = [ {101: 'Omar', 102: 'Esraa', 103: 'Ibrahim'} ]

print(len(persons_list))

print(persons_list[0])
#Esraa
print(persons_list[0][102])

print('----loop over dict keys / value----')
for key, value in persons_list[0].items():
    print(key)
    print(value)
    print('----')

print('add new dict to the list')
students_dict = {104: 'esam', 105: 'ayman', 106: 'hager'}
persons_list.append(students_dict)
print(persons_list)
#ayman
print(persons_list[1][105])



