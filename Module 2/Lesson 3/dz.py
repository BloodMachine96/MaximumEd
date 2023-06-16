# import random

# class Warrior():
#     def __init__(self, name, health):
#         self.health = health
#         self.name = name

#     def fight(self):
#         res = random.randint(1, 2)
#         if res == 1:
#             self.health -= 20
#         else:
#             print('Промах! ')

# warrior_1 = Warrior('Кратос', 100)
# warrior_2 = Warrior('Зевс', 100)

# while True:
#     question = input(f'Какой воин атакует, {warrior_1.name} (1) или {warrior_2.name} (2)? ')

#     if question == str(1):
#         print(f'{warrior_1.name} атакует {warrior_2.name + "а"}')
#         warrior_2.fight()
#         print(f'У противника осталось здоровья - {warrior_2.health}\n')
#     elif question == str(2):
#         print(f'{warrior_2.name} атакует {warrior_1.name + "а"}')
#         warrior_1.fight()
#         print(f'У противника осталось здоровья - {warrior_1.health}\n')

#     if warrior_1.health <= 0:
#         print(f'Игра окончена! {warrior_2.name} победил. ')
#         break
#     elif warrior_2.health <= 0:
#         print(f'Игра окончена! {warrior_1.name} победил. ')
#         break

from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

class Art:
    def __init__(self, color):
        self.color = color

    def build_art(self):
        canvas.create_rectangle(150, 50, 350, 250, fill=self.color, outline='red')
        canvas.create_rectangle(150, 250, 350, 450, fill=self.color, outline='blue')
        canvas.create_polygon(150, 50, 350, 175, 350, 50, fill=self.color, outline='red')
        canvas.create_polygon(150, 250, 350, 250, 150, 450, fill=self.color, outline='purple')

art_color = input('Введите цвет (на английском): ')

art_color_use = Art(art_color)

art_color_use.build_art()

window.mainloop()

