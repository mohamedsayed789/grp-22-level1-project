#H.w No. 4: # loop over all keys and raise the prices 10%
#Print sum of all the values after raise 10%
#Add vat 14$ to the total and print the net value
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
for key, value in shopping_cart_dict.items():
    print(key, value)
print('-----------------------------------------------------------------------------------------------')
# add the price 10%
total_price = 0
for key in shopping_cart_dict:
    shopping_cart_dict[key] = shopping_cart_dict[key] + 10 / 100 * shopping_cart_dict[key]
    total_price = total_price + shopping_cart_dict[key]
print('Ater raise 10% ' ,shopping_cart_dict, 'total price = ', total_price)
net_total_price = total_price + 14/100 * total_price
print('Net total price after 10% tax = ', net_total_price)

print('-----------------------------------------------------------------------------------------------')

total_shopping_cart_dict = shopping_cart_dict['milk'] + shopping_cart_dict['bread'] + shopping_cart_dict['eggs']
print(total_shopping_cart_dict)
print('-----------------------------------------------------------------------------------------------')

total_net = total_shopping_cart_dict + 14/100 * total_shopping_cart_dict
print(total_net)




