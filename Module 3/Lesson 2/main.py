import vk_api
import random
import requests
from bs4 import BeautifulSoup

def get_course():
    return soup.find("Valute", ID="R01235").Value.text

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, features="xml")

token = 'vk1.a.vKwWTiE_ATyQ7QBEKue-lniudDN8vHajKzt3dknFeZt7Gqx2mffe_FHVWtWo_SQJH99Ns15Gvn0FRZbINDJu5NHJS2OE3sysiGJotNiDPV-Hjgoe8mi_N1v47HTzBYtJBFZBKoWi5ba3zyyPG-fzFkx1F36qs62EJiQ3ddFL94nZUQYsE2DNi6yl-EbokjLqYJXeLfXf_7EpWi5wi2fm5A'

vk = vk_api.VkApi(token=token)

res = requests.get('https://swapi.dev/api/starships/').json()['results'] 

url = 'https://swapi.dev/api/'
response = requests.get(url).json()
print(response)
diameters_list = []
planet_api = response.get('planets')
def check_planets(url):
    for i in range(1,6):
        response = requests.get(f'{url}/{i}').json()
        diameters_list.append({response.get('name'): int(response.get('diameter'))})
    print(diameters_list)
check_planets(planet_api)
number = 0
diameter = 0
for i in range(len(diameters_list)):
    value = list(diameters_list[i].values())
    print(value)
    if value[0] > diameter:
        number = i
        diameter = value[0]

res = requests.get('https://swapi.dev/api/starships/').json()['results'] 

starships_answer = (max(((x['name'], x['max_atmosphering_speed']) for x in res),
    key=lambda x: int(x[1].replace('n/a', '0').replace('km', '')))[0])


while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] > 0:
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == "курс":
            ans = f"Курс доллара на сегодня составляет {get_course()} руб."
        elif message_text.lower() == "планеты":
            ans = f"Максимальный диаметр планеты {diameters_list[number]}"
        elif message_text.lower() == "корабли":
            ans = f"Самый быстрый корабль: {starships_answer}"
        else:
            ans = "Неизвестная команда"

        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10 ** 7, 10 ** 7)
            
        
        vk.method("messages.send", {
            "user_id": user_id,
            "random_id": random_id,
            "message": ans,
        })


#import vk_api
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# res = requests.get('https://swapi.dev/api/starships/').json()['results'] 

# url = 'https://swapi.dev/api/'
# response = requests.get(url).json()
# diameters_list = []
# planet_api = response.get('planets')
# def check_planets(url):
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()
#         diameters_list.append({response.get('name'): int(response.get('diameter'))})
# check_planets(planet_api)
# number = 0
# diameter = 0
# for i in range(len(diameters_list)):
#     value = list(diameters_list[i].values())
#     if value[0] > diameter:
#         number = i
#         diameter = value[0]

# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# today = datetime.today()
# today = today.strftime('%d/%m/%Y')
# payload = {'data_req': today}
# response = requests.get(url, params=payload)
# xml = BeautifulSoup(response.content, 'lxml')
# def getCourse(id):
#     return xml.find('valute', {'id':id}).value.text

# token = 'здесь мог быть ваш токен'

# vk = vk_api.VkApi(token=token)

# messages = vk.method("messages.getConversations", {"count": 20, "filter":"unanswered"})

# while True:
#     messages = vk.method("messages.getConversations", {"count": 20, "filter":"unanswered"})
#     if messages["count"]>=1:
#         user_id = messages["items"][0]["last_message"]["from_id"]
#         message_id = messages["items"][0]["last_message"]["id"]
#         message_text = messages["items"][0]["last_message"]["text"]
#         if message_text.lower() == 'привет':
#             vk.method("messages.send",{"peer_id": user_id, "random_id": message_id, "message": "Привет"})
#         elif message_text.lower() == 'курс':
#             vk.method("messages.send",{"peer_id": user_id, "random_id": message_id, "message": getCourse('R01235') })
#         elif message_text.lower() == 'планеты':
#             vk.method("messages.send",{"peer_id": user_id, "random_id": message_id, "message": diameters_list[number] })
#         elif message_text.lower() == 'корабли':
#             vk.method("messages.send",{"peer_id": user_id, "random_id": message_id, "message": max(((x['name'], x['max_atmosphering_speed']) for x in res),
#     key=lambda x: int(x[1].replace('n/a', '0').replace('km', '')))[0] })
#         else:
#             vk.method("messages.send",{"peer_id": user_id, "random_id": message_id, "message": "Неизвестная команда"})