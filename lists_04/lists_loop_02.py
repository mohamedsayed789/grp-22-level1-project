
my_list = [14, 7, 9, 2, 3, 10]

print("------ 1. loop using for i loop = we use the index----")
total = 0
for i in range( len(my_list) ):
    print( my_list[i] )
    total = total + my_list[i]

print("total of the numbers = " ,total)

print("------- 2. loops over the list using for each loop----- do not use index")
total = 0
for item in my_list:
    print(item)
    total = total + item

print("total of the numbers = " ,total)

print("-----3. using the builtin function sum() ------")
print(sum(my_list))


