# Count occurrences of a word in string: without using builtin function

statement = 'A computer science portal for portal'
word = 'portal'

# convert string to list

words_list = statement.split()
count_occur = 0
for item in words_list:
    if item == word:
        count_occur = count_occur + 1

print('word occur times : ', count_occur)


