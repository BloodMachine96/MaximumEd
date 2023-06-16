import random

# class A:
#     pass

# a1 = A()
# a2 = A()

# print(a1 is a2)

# class SingleTone:
#     __instance = None

#     def __new__(cls, *args, **kwargs): #cls - ссылка на весь класс
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)

#         return cls.__instance
    
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# a = SingleTone(10, 20)
# b= SingleTone(30,40)
# print(a is b)
# print(a.a, a.b)
# print(b.a, b.b)


# ----------------------
# decorators

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print('Прошло времени: ', time.time() - start)

#         return result
    
#     return wrapper

# @timer
# def get_list_by_default_way(val):
#     my_list = []
#     for i in range(val):
#         my_list.append(i)

#     return my_list

# @timer
# def get_list_by_list_comp(val):
#     my_list = [i for i in range(val)]
#     return my_list



# get_list_by_default_way(10 ** 6 * 15)
# get_list_by_default_way(10 ** 6 * 15)

age = 18

is_allow = True if age >= 18 else False

print(is_allow)