em_ids_list = [101, 102, 103]
em_names_list = ['ahmed', 'omar', 'sarah']

#create empty dictionary
persons_dict = {}

# loop over em ids list using for i index loop

for i in range(len(em_ids_list)):
    persons_dict[em_ids_list[i]] = em_names_list[i]    # add item to dict

print(persons_dict)
