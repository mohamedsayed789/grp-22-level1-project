# Write a program to Remove duplicated words – just leave unique words in a string – ignore case sensitive

statement = 'Hello world world python is great great Python'
words_list = statement.split()
unique_list = []
for item in words_list:
    if item not in unique_list:
        unique_list.append(item)
# convert from list to string
statement = " ".join(unique_list)
print(statement)
