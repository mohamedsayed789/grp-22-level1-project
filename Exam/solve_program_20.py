#Count occurrences of a word in string: without using builtin function

string = 'i like computer science python to python'
word = 'python'

new_list = string.split()
count_word = 0
for item in new_list:
    if item == word:
        count_word = count_word + 1

print('count word = ', count_word)

