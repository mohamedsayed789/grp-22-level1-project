# Using Lists
print('---- 1. Creating, Printing List ---- ')
my_list = [7,9,15,6,3]
print(my_list)
print(type(my_list))

print('---- 2. adding element to list [ append function , insert function ] --- ')
my_list.append(8)
my_list.insert(2 ,13)
print(my_list)

print('---- 3. Access element by index and change it -----')
print(my_list[3])
my_list[3] = my_list[3] + 2
print(my_list)


print('----- 4. count elements of list _ Len function : General Function -------')
print(len(my_list))

print('-------- 5. delete element from the list -- remove() , pop() functions -----')
#my_list.remove(3)  #delete element with the frist value = 3
my_list.pop(5)      #delete element with index = 5
print(my_list)

print('-------- 6. reverse list ----------')
my_list2 = my_list.copy()        # get backup from the list

my_list.reverse()
print("my_list2 " , my_list2)
print("my list " , my_list)



print('------- 7. sort list -------------')
my_list.sort()  # ascending
print(my_list)

my_list.sort(reverse=True)  # descending
print(my_list)
