# how to a loop over a dictionry
print('------1. loop over a dictionary keys using for each loop')
shopping_cart_disk = {'milk': 40.0, 'eggs': 160.0, 'bread': 30.0}

for key in shopping_cart_disk:
    print(key)
    print(shopping_cart_disk[key])  # value
    print('-----')

print('------2. loop over a dictionary key values using for each loop')
for key, value in shopping_cart_disk.items():
    print(key)
    print(value)
    print('----')

