from tkinter import *
import random

window = Tk()
window.geometry('600x600')
window.title('Уничтожение драконьего вида')
canvas = Canvas(window, width=600, height=600)
canvas.pack()

background = PhotoImage(file=r'D:\Разное\Игры и программы\Maximum\Module 2\Lesson 4\extra\bg_2.png')

class Warrior:
    def __init__(self):
        self.x = 150
        self.y = 350
        self.v = 0
        self.vx = 0
        self.photo = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 2\Lesson 4\extra\knight.png")

    def up(self, event):
        self.v = -5
    
    def down(self, event):
        self.v = 5

    def left(self, event):
        self.vx = -5
    
    def right(self, event):
        self.vx = 5
    
    def stop(self, event):
        self.v = 0
        self.vx = 0


knight = Warrior()

class Dragon():
    def __init__(self):
        self.x = random.randint(550, 600)
        self.y = random.randint(50, 550)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file=r'D:\Разное\Игры и программы\Maximum\Module 2\Lesson 4\extra\dragon.png')

dragons = []
for i in range(5):
    dragons.append(Dragon())

def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image= background)
    canvas.create_image(knight.x, knight.y, image= knight.photo)

    knight.y += knight.v
    knight.x += knight.vx
  
    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 544:
        knight.y = 543
    if knight.x <= 50:
        knight.x = 51
    if knight.x >= 550:
        knight.x = 551

    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image= dragon.photo)
        dragon.x -= dragon.v

        if ((knight.x - dragon.x) ** 2 + (knight.y - dragon.y) ** 2) ** 0.5 < 50:
            dragons.remove(dragon)

        if dragon.x <50:
            return lose()

    if len(dragons) == 0:
        return win()

    window.after(10, game)

def win():
    canvas.create_text(300, 300, text='Вы победили!', font='Verdana 42')

def lose():
    canvas.create_text(300, 300, text='Вы проиграли!', font='Verdana 42')


game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<Key-Left>', knight.left)
window.bind('<Key-Right>', knight.right)
window.bind('<KeyRelease>', knight.stop)

window.mainloop()