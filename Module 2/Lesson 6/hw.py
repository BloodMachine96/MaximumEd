import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today = datetime.today()
today = today.strftime('%d/%m/%Y')

payload = {'data_req': today}
response = requests.get(url, params=payload)

xml = BeautifulSoup(response.content, 'lxml')

ids = {'EUR':'R01239' , 'USD':'R01235', 'AUD':'R01010', 'AZN':'R01020A', 'GBP':'R01035', 'AMD':'R01060', 'BYN':'R01090B', 'BGN':'R01100', 'BRL':'R01115',
'HUF':'R01135', 'VND':'R01150', 'HKD':'R01200', 'GEL':'R01210', 'DKK':'R01215', 'AED':'R01230', 'EGP':'R01240', 'INR':'R01270', 'IDR':'R01280', 'KZT':'R01335',
'CAD':'R01350', 'QAR':'R01355', 'KGS':'R01370', 'CNY':'R01375', 'MDL':'R01500', 'NZD':'R01530', 'NOK':'R01535', 'PLN':'R01565', 'RON':'R01585F', 'XDR':'R01589', 
'SGD':'R01625', 'TJS':'R01670', 'THB':'R01675', 'TRY':'R01700J', 'TMT':'R01710A', 'UZS':'R01717', 'UAH':'R01720', 'CZK':'R01760', 'SEK':'R01770', 'CHF':'R01775',
'RSD':'R01805F', 'ZAR':'R01810', 'KRW':'R01815', 'JPY':'R01820'}

valute_from = input('Введите переводимую валюту: ')
valute_to = input('Введите желаемую валюту: ')
amount = float(input('Кол-во: '))


def getCourse(id):
    return xml.find('valute', {'id':id}).value.text

def getNominal(id):
    return xml.find('valute', {'id':id}).nominal.text


def course ():
    if valute_from != 'RUR':
        rur = float(getCourse(ids[valute_from]).replace(',', '.')) * int(getNominal(ids[valute_from])) * amount
        money = rur / float(getCourse(ids[valute_to]).replace(',', '.')) * int(getNominal(ids[valute_to]))
        print(money)
    elif valute_from == 'RUR':
        money = amount / float(getCourse(ids[valute_to]).replace(',', '.')) * int(getNominal(ids[valute_to]))
        print(money)

course()


# import requests
# from bs4 import BeautifulSoup


# response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=27/01/2022')
# soup = BeautifulSoup(response.content, features='xml')
# #  print(response.content)


# def get_course():
#     australian_dollar= soup.find('Valute', ID='R01010')
#     usd = soup.find('Valute', ID='R01235')
#     eur = soup.find('Valute', ID='R01239')

#     currency_nominal =(australian_dollar.Nominal.text)
#     currency_value = (australian_dollar.Value.text)
#     currency_name = (australian_dollar.Name.text)

#     currency_nominal2 =(usd.Nominal.text)
#     currency_value2 = (usd.Value.text)
#     currency_name2 = (usd.Name.text)

#     currency_nominal3 =(eur.Nominal.text)
#     currency_value3 = (eur.Value.text)
#     currency_name3 = (eur.Name.text)

#     print(f'({currency_nominal} шт.) {currency_name}, стоит(ят) {currency_value} руб.')
#     print(f'({currency_nominal2} шт.) {currency_name2}, стоит(ят) {currency_value2} руб.')
#     print(f'({currency_nominal3} шт.) {currency_name3}, стоит(ят) {currency_value3} руб.')

# get_course()