dict1 = {'a': 100, 'b': 150, 'c': 100}
dict2 = {'a': 50, 'c': 100, 'd': 150}

#loop over dict2

for key, value in dict2.items():
    if key in dict1:    #key found add both values
        dict1[key] = dict1[key] + dict2[key]
    else: # key not found then add new key , value
        dict1[key] = dict2[key]

print(dict1)

