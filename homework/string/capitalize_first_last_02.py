# Write a Python program to capitalize the first and last letters of each word in a given string.

statement = "python exercises practice solution"
print('Original Statement, ', statement)
statement = statement.title() # capitalize the first letter

# convert string to words list
words_list = statement.split()

for i in range(len(words_list)):
    words_list[i] = words_list[i][:-1] + words_list[i][-1].upper()

statement = ' '.join(words_list)
print('After Convert, ', statement)
