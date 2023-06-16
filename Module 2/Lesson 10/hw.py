class User:
    def __init__(self, health):
        self.health = health

    def attack(self, target):
        target.take_damage # реализация атаки

    def take_damage(self, damage):
        self.health -= damage # уменьшение здоровья на величину damage

class Mage(User):
    def __init__(self, health, mana):
        super().__init__(health)
        self.mana = mana
    
    def mana_cost(self, spell_mana, mana):
        spell_mana = 5
        mana -= spell_mana

    def cast_spell(self, spell_name, target):
        spell_name = input('Выберите заклинание (искра): ')
        
        if spell_name != 'Искра':
            damage = 5
            target.take_damage(damage)
        elif spell_name != 'Фаерболл':
            damage = 10
            target.take_damage(damage)
        else:
            print('Ошибка')


class Warrior(User):
    def __init__(self, health, strength):
        super().__init__(health)
        self.strength = strength

    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)


class Archer(User):
    def __init__(self, health, agility):
        super().__init__(health)
        self.agility = agility

    def shoot_arrow(self, target):
        damage = self.agility
        target.take_damage(damage)

mage = Mage(100, 30)
warrior = Warrior(100, 35)
archer = Archer(100, 20)

def the_choose():
    choose = input('Выберите свой класс (mage/warrior/archer): ')
    enemy_choose = input('Выберите цель(mage/ archer/ warrior): ')
    if choose == 'mage':
        mage.cast_spell(enemy_choose)
    elif choose == 'warrior':
        warrior.attack(enemy_choose)
    elif choose == 'archer':
        archer.shoot_arrow(enemy_choose)
    else:
        print('error')

the_choose()


#     class User:
#     def __init__(self, hp, armor, damage):
#         self.hp = hp
#         self.armor = armor
#         self.damage = damage

#     def attack(self, enemy):
#         enemy.health_down(self.damage)
#         print(f'Вы попали по противнику: {enemy}')

#     def health_down(self, damage):
#         print(f'Урон:{damage}')
#         total_damage = damage / self.armor
#         self.hp -= total_damage
 
# class Mage(User): 
#     def __init__(self, hp, armor, damage):
#         super().__init__(hp, armor, damage)
    
#     def cast_spell(self, enemy): 
#         enemy.attack(self.damage) 
 
# class Warrior(User): 
#     def __init__(self, hp, armor, damage):
#         super().__init__(hp, armor, damage)

#     def swing_sword(self, enemy): 
#         enemy.attack(self.damage) 
 
# class Archer(User): 
#     def __init__(self, hp, armor, damage):
#         super().__init__(hp, armor, damage)

#     def shoot_arrow(self, enemy): 
#         enemy.attack(self.damage) 

# mage = Mage(100, 5, 30)
# warrior = Warrior(100, 15, 25)
# archer = Archer(100, 10, 20)

# mage.cast_spell(warrior)
