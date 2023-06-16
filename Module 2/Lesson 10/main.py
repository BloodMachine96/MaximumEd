
class Frog:
    name = 'Пе-пе'
    animal = 'Лягушка'


print(Frog(), Frog().sound)

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

vanya = People('vanya', 18)
dima = People('dima',17)