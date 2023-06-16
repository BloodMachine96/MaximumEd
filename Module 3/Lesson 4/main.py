from contextlib import contextmanager
# import time

# def e():
#     for i in range(1,11):
#         print(f"До {i}")
#         yield i
#         print(f"После {i}")

# for i in e():
#     print(i)

# generator = [i**2 for i in range(1000000)]
# print(generator)

# def generator():
#     for i in range(100000):
#         yield i**2




# start = time.time()
# my_list = (time.sleep(x) for x in range(1, 3))

# for i in my_list:
#     print(i)

# print(time.time() - start)

# def generator():
#     for i in range(1,1000001):
#         print(f"До {i}")
#         yield i**2
#         print(f"После {i}")

# for i in generator():
#     print(i)




# def my_lazy_func():
#     for i in range(1,11):
#         yield i

# for i in my_lazy_func():
#     print(i)

# def my_lazy_func(items):
#     for i in items:
#         yield i ** 2

# def my_lazy_func(items):
#     yield from (i**2 for i in items)

# for i in my_lazy_func(1):
#     print(i)

# f = open('test.txt', 'w', encoding = 'utf-8')
# f.write('Скоро лето...')
# f.close

# with open('text.txt', 'w', encoding='utf-8') as f:
#     f.write('Скоро лето, а сейчас весна')
#     print(f.closed)
# print(f.closed)

# my_list = [1,2]

# @contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print('Была ошибка, но мне всё равно')

# with exc_handler(IndexError):
#     my_list[4]

# my_gen = (x**2 for x in range(1001))

# for i in my_gen:
#     print(i)

# def gen():
#     for i in range(1001):
#         yield i**2

# for i in gen():
#     print(i)

from contextlib import contextmanager
from bs4 import BeautifulSoup
import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, features='xml')

id = str(input('Введите ID желаемой валюты: '))

xml = BeautifulSoup(response.content, 'xml')

ids = ['R01239','R01235','R01010','R01020A','R01035','R01060','R01090B','R01100','R01115','R01135',
'R01150','R01200','R01210','R01215','R01230','R01240','R01270','R01280','R01335','R01350','R01355',
'R01370','R01375','R01500','R01530','R01535','R01565','R01585F''R01589', 'R01625','R01670','R01675',
'R01700J','R01710A','R01717','R01720','R01760','R01770','R01775','R01805F','R01810','R01815','R01820']

def getNominal(id):
    return xml.find('Valute', ID=id).Nominal.text
def getCourse(id):
    return xml.find('Valute', ID=id).Name.text
def getValue(id):
    return xml.find('Valute', ID=id).Value.text


@contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        print('Была ошибка, но мне всё равно')


def get_course_info(id):
    if id in ids:
        yield f'({getNominal(id)} шт.) {getCourse(id)} стоит(ят) {getValue(id)} руб.'
    else:
        print("Произошла ошибка")


with get_course_info(id) as currency:
    print(currency)