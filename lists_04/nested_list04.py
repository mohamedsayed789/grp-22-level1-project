my_list = [
             [101, 'ahmed' , 'cairo'],
            [102, 'omar' , 'alex'],
            [103, 'ibrahim' , ['cairo' , 'nasr city ', 'abbas el akkad']]
           ]

print(my_list)
#print the first element [101, 'ahmed' , 'cairo']
print(my_list[0])

#print alex
print(my_list[1][2])

#print nasr city
print(my_list[2][2][1])

#add this list to my-list

new_person = [104 , 'amir' , 'gharbeya']
my_list.append(new_person)
print(my_list)


