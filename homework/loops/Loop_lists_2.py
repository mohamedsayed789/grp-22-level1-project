# Loop over 2 lists, and print this result

list1 = [5, 10, 15, 20]
list2 = ['Tomatoes', 'Potatoes', 'Caroots', 'Cucumbers']

for i in range(len(list1)):
    for j in range(len(list2)):
        print(list1[i], list2[j])

