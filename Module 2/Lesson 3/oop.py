from tkinter import *
import time

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg="white")
canvas.pack()


class House:
    def __init__(self, windows, color):
        self.square = 2000
        self.windows = windows
        self.color = color

    def build_house(self):
        canvas.create_rectangle(150, 150, 400, 400, fill=self.color, outline='red')
        canvas.create_polygon(150, 150, 275, 75, 400, 150, fill=self.color, outline='red')

    def __str__(self):
        return f'Площадь дома {self.square}, кол-во окон: {self.windows}'

    def __add__(self, other):
        return self.square + other.square


house1 = House(2000, 'red')
house2 = House(200, 'blue')
house3 = House(20, 'orange')

# print(house1.windows, house2.windows, house3.windows)
# print(house1.square, house2.square, house3.square)

# house1.windows = 3000
# print(house1.windows)

print(house1)
print(house2)
print(house3)
print(house1 + house2)

window.mainloop()