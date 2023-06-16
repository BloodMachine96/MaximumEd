import requests

response = requests.get('https://swapi.dev/api/')
planets_url = response.json()['planets']

response = requests.get(planets_url)
print(response.json())

planets_list = []

for i in range (1,6):
    detail_planet_url = f'{planets_url}{i}'
    response = requests.get(detail_planet_url)
    data = response.json()
    data['diameter'] = int(data['diameter'])
    planets_list.append(data)

    planets_list.append(response.json())

    print(response.json())

# max_value = 0
# for planet in planets_list:
#     if planet['diameter'] > max_value:
#         max_value = planet['diameter']
    
# for planet in planets_list:
#     if max_value == planet['diameter']:
#         print(planet)
#         break

print(max(planets_list, key=lambda x: x['diameter']))

# print(planets_list['diameter'])

# 200 - good
# 404 - error
# 201 - e
