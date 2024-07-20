# Converting a List of Tuples to a Dictionary
colors_list = [ ('red', 223), ('blue', 201), ('green', 210) ]

colors_dict = {}

for item in colors_list:
    print(item, item[0], item[1] )
    colors_dict[item[0]] = item[1]
    print('----')

print(colors_dict)
































