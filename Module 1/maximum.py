list_of_buy = ['Капуста', 'Яйца', 'Молоко', 'Хлеб', 'Бананы']
print('Изначальный список: ', list_of_buy)
list_of_buy.append('Помидоры')
print('Список после добавления пункта: ', list_of_buy)
list_of_buy[1] = 'Колбаса'
print('Список после замены воторого пункта: ', list_of_buy)
print('Длина списка: ', len(list_of_buy))
list_of_buy.sort()
print('Список после сортировки по алфавиту: ', list_of_buy)
del list_of_buy[5]
