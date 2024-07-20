# Make Uppercase Half String

statement = 'ArabRepublicOfEgypt'
# printing original string
print("The original string is : " + statement)

half_len = len(statement) / 2
half_len = int(half_len)
statement = statement[:half_len].lower() + statement[half_len:].upper()

# printing result
print("The final string : " + statement)
