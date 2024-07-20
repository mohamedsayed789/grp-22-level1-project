# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart_disk = {'milk': 40.0, 'eggs': 160.0, 'bread': 30.0}
print(shopping_cart_disk)
print(type(shopping_cart_disk))
print(len(shopping_cart_disk))


print('------ Adding, change new pair to the dictionary -------')
shopping_cart_disk['nescafe'] = 60.0
shopping_cart_disk['milk'] = 45.0
print(shopping_cart_disk)


print('------ access element -----')
print('price of eggs = ', shopping_cart_disk['eggs'])
#add 25% to the price of eggs
shopping_cart_disk['eggs'] = shopping_cart_disk['eggs'] + 25/100 * shopping_cart_disk['eggs']
print(shopping_cart_disk)


print('---- delete element pair from dict ------')
shopping_cart_disk.pop('bread')
print(shopping_cart_disk)

print('------ Concat Multi dictionaries ------')
home_cart_dict = {'meat': 400.0, 'chicken': 125.0, 'milk': 60.0}
shopping_cart_disk.update(home_cart_dict)
print(shopping_cart_disk)