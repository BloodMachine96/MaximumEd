# Инкапсуляция - это принцип в осглве которого лежит защита данных в нашем классе
# Полеморфизм - ?
# Наследование - это принцип в основе которого лежит наследование атрибутов класса


# Магический метод __add__:
#         Теория
# Метод __add__ - это магический метод класса, который определяет поведение класса, когда мы его с чем-либо складываем
# Метод принимает два параметра: self и other(Другой объект)

#         Важно
# 19 число отпросить с курсов
# ChatGPT or You.com


#         Практика


class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price 
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
    
    def __radd__(self,other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, int):
            self.price - other

    def __truediv__(self, other):
        if isinstance(other, Item):
            return self.price / other.price
        elif isinstance(other, int):
            return self.price / other
        else:
            raise ValueError("Цену на цену незя")
    
    def __mul__(self, other):
        if isinstance(other,Item):
            return self.price * other.price
        elif isinstance(other, int):
            return self.price * other

item1 = Item('Процессор', 15_000, 0.2)
item2 = Item('Видеокарта', 30_000, 0.9)
item3 = Item('Оперативка', 8000, 0.5)

# Можно сложить через item1.price + item2.price

# total_sum = item1 + item2

# total_sum = 1000 + item1 
#Компьютеру важно в каком порядке слагаемые
print(item2/item1)
print(item3-item1)
print(item2*2)
print(item2/item3)
print(item3/2)

