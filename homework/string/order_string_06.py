# Write a program that takes an input string and displays
# its letters in alphabetical order. For instance,
# if the input is "Python", the output should be "Phnoty"

statement = 'Python'
print('Original : ', statement)
# convert string to List of letters
letters_list = []
for letter in statement:
   letters_list.append(letter)

# sort list in Asc
letters_list.sort()

# Back from list to string
statement = ' '.join(letters_list)
print('After Sort : ', statement)



