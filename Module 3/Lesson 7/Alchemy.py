from tkinter import *
import random

window = Tk()
window.geometry("600x600")
window.title("Алхимик из шестёрочки")

canvas = Canvas(width=600, height=600)
canvas.pack()

class Steam:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\aroma.png").subsample(4,4)

class Pottery:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\pottery.png").subsample(4,4)

class Dust:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\dust.png").subsample(4,4)

class Mud:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\mud.png").subsample(4,4)

class Water:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\water.png").subsample(4,4)

    def __add__(self,other):
        if isinstance(other, Fire):
            return Steam
        elif isinstance(other, Earth):
            return Mud


class Fire:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\fire.png").subsample(4,4)

    def __add__(self,other):
        if isinstance(other, Water):
            return Steam
        elif isinstance(other, Fire):
            return Pottery

class Wind:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\wind.png").subsample(4,4)

    def __add__(self,other):
        if isinstance(other, Earth):
            return Dust


class Earth:
    image = PhotoImage(file=r"D:\Разное\Игры и программы\Maximum\Module 3\Lesson 7\Доп. материалы\ground.png").subsample(4,4)
    
    def __add__(self,other):
        if isinstance(other, Wind):
            return Dust
        elif isinstance(other, Water):
            return Mud
        elif isinstance(other, Fire):
            return Pottery


elements = [Wind(), Fire(), Water(), Earth()]

for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50,550), image=elem.image)

def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 = images_ids[0], images_ids[1]
        elem_1 = elements[elem_id_1 - 1]
        elem_2 = elements[elem_id_2 - 1]

        new_elems = elem_1 + elem_2
        if new_elems not in elements:
            elements.append(new_elems)
            canvas.create_image(event.x, event.y, image=new_elems.image)

    canvas.coords(images_ids, event.x, event.y)

window.bind("<B1-Motion>", move)

window.mainloop()