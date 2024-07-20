# loop over all keys and raise the prices 10%
#Print sum of all the values after raise 10%
#Add vat 14% to the total and print the net value
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}

for key, value in shopping_cart_dict.items():
    print(key, value)

total_price = 0
for key in shopping_cart_dict:
    shopping_cart_dict[key] = shopping_cart_dict[key] + 10 / 100 * shopping_cart_dict[key]
    total_price = total_price + shopping_cart_dict[key]
print('raise 10% = ' ,shopping_cart_dict)
('total price = ', total_price)

total_shopping_cart_dict = shopping_cart_dict['milk'] + shopping_cart_dict['bread'] + shopping_cart_dict['eggs']
print('total shopping cart dict = ', total_shopping_cart_dict)

net_value = total_shopping_cart_dict + 14/100 * total_shopping_cart_dict
print('net value = ', net_value)
