# Join multi tuples into 1 dictionary – Beginner – without loop
person_1_tuples = (101, 'ahmed esam', 5000.0, 'cairo', '0127454104')
person_2_tuples = (102, 'mohamed omar', 6000.0, 'alex', '01147041564')
person_3_tuples = (103, 'ibrahim hesham', 7000.0, 'portsaid', '01032659878')

person_dict = {}

new_person = person_1_tuples + person_2_tuples + person_3_tuples

person_dict['person 1'] = person_1_tuples
person_dict['person 2'] = person_2_tuples
person_dict['person 3'] = person_3_tuples
print(person_dict)








