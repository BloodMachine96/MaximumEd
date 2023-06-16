import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import requests
from bs4 import BeautifulSoup
import wikipedia

def get_article(article):
    wikipedia.set_lang("ru")

    try:
        return wikipedia.summary(article)
    except wikipedia.WikipediaException:
        return "По данному запросу ничего не нашлось"

def get_course(course_id):
    return soup.find("Valute", ID=course_id).Value.text

ids = {'EUR':"R01239" , 'USD':'R01235', 'AUD':'R01010', 'AZN':'R01020A', 'GBP':'R01035', 'AMD':'R01060', 'BYN':'R01090B', 'BGN':'R01100', 'BRL':'R01115',
'HUF':'R01135', 'VND':'R01150', 'HKD':'R01200', 'GEL':'R01210', 'DKK':'R01215', 'AED':'R01230', 'EGP':'R01240', 'INR':'R01270', 'IDR':'R01280', 'KZT':'R01335',
'CAD':'R01350', 'QAR':'R01355', 'KGS':'R01370', 'CNY':'R01375', 'MDL':'R01500', 'NZD':'R01530', 'NOK':'R01535', 'PLN':'R01565', 'RON':'R01585F', 'XDR':'R01589', 
'SGD':'R01625', 'TJS':'R01670', 'THB':'R01675', 'TRY':'R01700J', 'TMT':'R01710A', 'UZS':'R01717', 'UAH':'R01720', 'CZK':'R01760', 'SEK':'R01770', 'CHF':'R01775',
'RSD':'R01805F', 'ZAR':'R01810', 'KRW':'R01815', 'JPY':'R01820'}

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, features="xml")

token = 'vk1.a.vKwWTiE_ATyQ7QBEKue-lniudDN8vHajKzt3dknFeZt7Gqx2mffe_FHVWtWo_SQJH99Ns15Gvn0FRZbINDJu5NHJS2OE3sysiGJotNiDPV-Hjgoe8mi_N1v47HTzBYtJBFZBKoWi5ba3zyyPG-fzFkx1F36qs62EJiQ3ddFL94nZUQYsE2DNi6yl-EbokjLqYJXeLfXf_7EpWi5wi2fm5A'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id
        if user_message[:2] == '-к':
            response = f"Курс выбранной вами валюты в рублях составляет: {get_course(ids[user_message[3:].upper()])} руб."
        elif user_message[:2] == '-в':
            article = user_message[2:]
            response = get_article(article)
        else:
            response = 'Такой команды я не знаю'
        vk.messages.send(
            user_id = user_id,
            message = response,
            random_id = random.randint(-10**7, 10**7)


        )
exm = ids.get('EUR')