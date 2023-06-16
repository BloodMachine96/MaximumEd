from tkinter import *

window = Tk()
window.geometry("500x400")
window.title('Аркада')
window.resizable(width=False,height=False)

canvas = Canvas(window, width=500, height=400)

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval()
        self.x = 1
        self.y = 1

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        coords = self.canvas.coords()

        x1, y1, x2, y2 = coords
        if x1 <= 0 or x2 >= 500:
            self.x = -self.x
        if y1 <=0 or x2 >= 400:
            self.y = -self.x


ball = Ball(canvas, 'red')



# while True:
#     window.update()
#     time.sleep(0.01)

