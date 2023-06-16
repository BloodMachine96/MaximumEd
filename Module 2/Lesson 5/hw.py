# import requests

# response = requests.get('https://swapi.dev/api/')
# starships_url = response.json()['starships']

# response = requests.get(starships_url)
# print(response.json())

# starships_list = []

# for i in range (1,6):
#     detail_starships_url = f'{starships_url}{i}'
#     response = requests.get(detail_starships_url)
#     data = response.json()
#     data['max_atmosphering_speed'] = int(data['max_atmosphering_speed'])
#     starships_list.append(data)

#     starships_list.append(response.json())

#     print(response.json())

# max_value = 0
# for planet in planets_list:
#     if planet['diameter'] > max_value:
#         max_value = planet['diameter']
    
# for planet in planets_list:
#     if max_value == planet['diameter']:
#         print(planet)
#         break

# print(max(starships_list, key=lambda x: x['max_atmosphering_speed']))

# import requests

# url = 'https://swapi.dev/api/'
# response = requests.get(url).json()
# ships = []

# starships_api = response.get('starships')
# def max_atmosphering_speed(url):
#     for i in range(9,14):
#         response = requests.get(f'{url}/{i}').json()
#         ships.append({response.get('name'): response.get('max_atmosphering_speed')})
#     print(ships)


# max_atmosphering_speed(starships_api)

import requests

url = 'https://swapi.dev/api/'
response = requests.get(url).json()
ships = []

starships_api = response.get('starships')
def max_atmosphering_speed(url):
    for i in range(9, 14):
        response = requests.get(f'{url}/{i}').json()
        ships.append({response.get('name'): response.get('max_atmosphering_speed')})
    print(ships)


max_atmosphering_speed(starships_api)
