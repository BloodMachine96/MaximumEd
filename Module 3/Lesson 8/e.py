# if __name__ == "__main__":

    # goods = [

    #     {
    #         "name": 'Iphone 7',
    #         'brand': 'Apple',
    #         'price': 100
    #     },
    #     {
    #         'name':'Ipad',
    #         'brand':'Apple',
    #         'price':50
    #     },
    #     {
    #         'name':'Windows XP',
    #         'brand':'Microsoft',
    #         'price':150
    #     }
    # ]

    # def on_price(item):
    #     return item['price']

    # print(sorted(goods, key=lambda x: x['price'])) #Можно вместо x написать что угодно т.к. это переменная(i)

    # print(list(filter(lambda x: x['brand'] == 'Apple', goods)))

#     numbers = ['1', '2', '3', '4', '5']
#     print(list(map(int, numbers)))

#     names_list = ['Igor', 'Артем', 'Аня', 'Ксюша']
#     surnames = ['Иванов', 'Петрович', 'Максимовна', 'Андреевна']

#     persons = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames))
#     print(list(persons))

#     # for i in range(len(spisok)):
#     #     ... - раньше

#     # for index, item in enumerate(goods):
#     #       print(index, item)

#     # for item, price in zip(goods, prices):
#     #         print(item, price)

#     new_goods = []

#     for index, item in enumerate(goods):
#         new_goods.append({index: item})

#     print(new_goods)

#     for name in zip(names_list, surnames):
#         print(name,surnames)

#     print(__name__)

# else:
#     print('Скрип запустился извне')








# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

#     def __repr__(self):
#         return self.brand
    
# items_list = [
#     Item(1000, "Apple"),
#     Item(1200, "Apple"),
#     Item(900, "Samsung"),
#     Item(700,"Samsung"),
#     Item(660, "Xiaomi"),
# ]

# print(list(filter(lambda x: x.brand == 'Apple', items_list)))

names_list = ['данил', 'артём', 'никита', 'влад']
print(list(map(lambda x: x.capitalize(), names_list)))

# from contextlib import contextmanager
# from bs4 import BeautifulSoup
# import requests

# response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, features='xml')

# id = str(input('Введите ID желаемой валюты: '))

# xml = BeautifulSoup(response.content, 'xml')

# ids = ['R01239','R01235','R01010','R01020A','R01035','R01060','R01090B','R01100','R01115','R01135',
# 'R01150','R01200','R01210','R01215','R01230','R01240','R01270','R01280','R01335','R01350','R01355',
# 'R01370','R01375','R01500','R01530','R01535','R01565','R01585F''R01589', 'R01625','R01670','R01675',
# 'R01700J','R01710A','R01717','R01720','R01760','R01770','R01775','R01805F','R01810','R01815','R01820']

# def getNominal(id):
#     return xml.find('Valute', ID=id).Nominal.text
# def getCourse(id):
#     return xml.find('Valute', ID=id).Name.text
# def getValue(id):
#     return xml.find('Valute', ID=id).Value.text

# @contextmanager
# def get_course_info(id):
#     if id in ids:
#         yield f'({getNominal(id)} шт.) {getCourse(id)} стоит(ят) {getValue(id)} руб.'
#     else:
#         print('Такая валюта не найдена.')
        

# with get_course_info(id) as currency:
#     print(currency)