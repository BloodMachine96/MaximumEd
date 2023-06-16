import requests
from bs4 import BeautifulSoup

course_date = input('Введите дату в формате dd/mm/yyyy: ')

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={'date_req': course_date})
soup = BeautifulSoup(response.content, features='xml')

currincies_list = soup.find_all('Valute')

user_currency = input('Введите букву/последовательность букв с которых начинается название валюты: ').upper()

for currency in currincies_list:
    currency_nominal =(currency.Nominal.text)
    currency_value = (currency.Value.text)
    currency_name = (currency.Name.text)

    if currency_name.startswith(user_currency):
        print(f'({currency_nominal} шт.) {currency_name}, стоит(ят) {currency_value} руб.')

