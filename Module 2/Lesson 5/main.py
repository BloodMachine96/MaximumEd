
a=10
b=20

if a>b:
    print('True')
else:
    print('False')

# print (a<b)

# end

d = 40
f = 50

if f>d and b>a:
    print('True')
else:
    print('False')

# or

if f<d or b>a:
    print('True')
else:
    print('False')

# not

if not (f<d or b>a):
    print('True')
else:
    print('False')

# Проверка логических строений данных

# Если вписать данные, то true, иначе false

my_str = 'какая-то инфа'

my_list = [1]

my_dict = {'key': 'value'}

if my_dict:
    print('True')
else:
    print('False')

'https://swapi.dev/api/'