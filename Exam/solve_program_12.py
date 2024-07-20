#program to reverse a string words
str = 'i like this program very much'

new_list = str.split()
new_list.reverse()
str = ' '.join(new_list)
print(str)

