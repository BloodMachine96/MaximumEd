# def my_func(*args, **kwargs):
#     print(*args)
#     a = kwargs.get('a')
#     print(a)

# my_func(10,20,30,'привет мир', a=10)
# позиционные сначала, потом именованные

# age = 18

# criminal_record = False

# is_allow = 'Можно' if age >= 18 and not criminal_record else 'Нельзя'

# print(is_allow)

# a = 100
# b = 1000

# c = a or b #При or выбирать всё, что не ложь

# print(c)

# my_list = []

# for i in range(1000):
#     my_list.append(i)

# print(my_list)

# my_list = [i if i % 5 == 0 else i * 5 for i in range(1000) if i % 3 == 0]
# print(my_list)

# my_dictionary = {i: len(i) for i in ['первый', "второйй", "третийq"] if len(i) != 6}
# print(my_dictionary)

# my_list1 = [1,2]
# my_list2 = [1,2]

# print(my_list1 == my_list2) #is - сравнить на одинаковость объекстов(один и тот же)

# a = 10
# b= 10

# print(a is b)

# print(id(my_list1), id(my_list2))

# my_tuple = (1, 2, 3, 4)
# print(my_tuple)
# print(type(my_tuple))
# element = my_tuple[2]
# print(element)

# my_dict = {
#     ('Чечевицын', 'Степан'): '+71291233456'

# }

# print(my_dict)
# print(sorted(my_tuple))

# my_tuple = (i for i in range(0, 1000))
# print(my_tuple)



#DЗ:

# my_list1 =[i for i in range(10) if i % 2 == 0] 
# my_list2 =[i for i in range(10) if i % 2 == 1]
# print(my_list1, my_list2)

# a = (5, 3, 2, 1, 4)
# print(tuple(sorted(a)))
