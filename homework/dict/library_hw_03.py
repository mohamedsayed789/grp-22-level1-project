book_dict = {'pages': 227, 'name': 'gone girl', 'year': 2007}

book_dict['author'] = 'well max'
print(book_dict)
print('---------------------------------------------------------------------------')
print('name', book_dict['name'])
print('---------------------------------------------------------------------------')
book_dict['year'] = 2010
print(book_dict)
print('---------------------------------------------------------------------------')
for key, value in book_dict.items():
    print(key, value)
print('---------------------------------------------------------------------------')
book_dict.pop('name')
print(book_dict)





