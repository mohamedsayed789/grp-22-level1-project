# Create a Python function to check if a string is a palindrome Return True or False
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

# main program
statement = 'radar'

if is_palindrome(statement):
    print('Yes, it is palindrome')
else:
    print('No, it is not palindrome')

