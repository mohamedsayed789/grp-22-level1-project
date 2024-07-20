#Remove all characters except letters and numbers
ini_string = "123abcjw:, .@! eiw"

new_string = ''

for letter in ini_string:
    if letter.isalnum():
        new_string = new_string + letter
print(new_string)



