from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

class Art:
    def __init__(self, color):
        self.color = color

    def build_art(self):
        canvas.create_rectangle(150, 50, 350, 250, fill=self.color, outline='black')
        canvas.create_rectangle(150, 250, 350, 450, fill=self.color, outline='black')
        canvas.create_polygon(150, 50, 350, 175, 350, 50, fill=self.color, outline='black')
        canvas.create_polygon(150, 250, 350, 250, 150, 450, fill=self.color, outline='black')

art_color = input('Введите цвет (на английском): ')

art_color_use = Art(art_color)

art_color_use.build_art()

window.mainloop()