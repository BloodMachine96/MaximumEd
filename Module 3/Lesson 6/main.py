# set(get)_(Название атрибута). Находятся в классе, медот, но выполняют строго заданное действие.

# class Year:
#     def __init__(self):
#         self.__days= 365
    
#     def get_days(self):
#         return self.__days
    
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise ValueError(f"Некорректное значение атрибута: {days}")
        
# year = Year()
# print(year.get_days())
# year.set_days(366)
# print(year.get_days())
# year.set_days(367)

# class Year:
#     def __init__(self, days):
#         self.days = days
    
#     @property
#     def days(self):
#         return self.__days
    
#     @days.setter
#     def days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception(f"Некорректное значение атрибута: {days}")
        
# year = Year(365)
# print(year.days)
# year.days = 363
# print(year.days)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def age(self):
        return self.__age
    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, age):
        if age == None or age>=0:
            self.__age = age
        else:
              raise Exception('Неккоректное значение')

    @name.setter
    def name(self, name):
        self.__name = name

    @age.deleter
    def age(self):
        print('Возраст удалён')
        self.__age = None
    @name.deleter
    def name(self):
        print('Имя удалено!')
        self.__age = None

person = Person("Максим", 16)
del person.age
print(person.age)
del person.name
print(person.name)


# 1111111
# 711

# my_l = [1,2,3]

# class MyList(list):
#     def delete_last_elem(self):
#         self.remove(self[-1])

# my_list = [x*10 for x in 'привет, мир!']
# for sym in my_list:
#     print(sym)
