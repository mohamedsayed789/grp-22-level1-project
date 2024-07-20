# program to reverse a string words

statement = "i like this program very much"
# output : 'much very program this like i'

# print( statement[::-1]) # reverse letters XXX

"""
1. convert string to list ( split() )
2. use reverse in list
3. join() list to string 
"""
words_list = statement.split()
print(words_list)
words_list.reverse()
print(words_list)
statement = ' '.join(words_list)
print(statement)
