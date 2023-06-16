import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime('%d.%m.%Y') #маркер
# print(today)
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={'date_req': today})

def get_course(currency_id):
    soup = BeautifulSoup(response.content, features='xml')
    valute = soup.find('Valute', ID= currency_id)
    name = valute.Name.text
    value = valute.Value.text

    valute_info = {
        'name': name,
        'value': value
    }

    return valute_info


print(get_course('R01010'))#обращаясь к словарю, можно использовать функции 