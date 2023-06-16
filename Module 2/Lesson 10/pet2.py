# class Pet:
#     def __init__(self, has_tail, legs, name, animal):
#             self.has_tail = has_tail
#             self.legs = legs
#             self.name = name
#             self.animal = animal

#     def __str__(self):
#         result = f'Питомец {self.name}. Это {self.animal}' \
#         f"У него {'есть хвост' if self.has_tail else 'хвоста нет'}. У него {self.legs} ног(и)"
        
#         return result
    

#     def sound(self):
#         pass

# class Dog(Pet):
#     def __init__(self, has_tail, legs, name):
#         super().__init__(has_tail, legs, name, 'Собака')

# dog = Dog(True, 4, 'Чарли')

# class Tank:
#     def __init__(self, hp, armor, damage):
#         self.hp = hp
#         self.armor = armor
#         self.damage = damage

#     def shoot(self, enemy):
#         enemy.health_down(self.damage)
#         print(f'Мы выстрелили по {enemy}')

#     def health_down(self, damage):
#         print(f'По нам попали, урон:{damage}')
#         total_damage = damage / self.armor
#         self.hp -= total_damage


# class T34(Tank):
#     def __str__(self):
#         return 'T34'
        
# class ATTV(Tank):
#     def __init__(self, hp, armor, damage):
#         super().__init__(hp, armor * 10, damage * 100)

#     def __str__(self):
#         return 'ATTV'

# t34 = T34(1000, 1500, 200)
# attv = ATTV(1000, 500, 100)

# t34.shoot(attv)
# attv.shoot(t34)

class user:
    def __init__(self, hp, armor, damage):
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def attack(self, enemy):
        enemy.health_down(self.damage)
        print(f'Вы попали по {enemy}. Урон: {self.damage}')

    def health_down(self, damage):
        print(f'По вам попали, урон:{damage}')
        total_damage = damage / self.armor
        self.hp -= total_damage

class Mage(user):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
    
    def cast_spell():
        pass

    def __str__(self):
        return 'Mage'
    
class Warrior(user):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
    
    def __str__(self):
        return 'Warrior'
    
class Archer(user):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor, damage)
    
    def __str__(self):
        return 'Archer'

mage = Mage(100, 20, 70) 
warrior = Warrior(150, 35, 60)
archer = Archer(125, 25, 50)

mage.attack(warrior)

