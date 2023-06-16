from main import get_course, today
from tkinter import *

window = Tk()
window.geometry('500x500')
window.resizable(width=False,height=False)
window.config(bg='lightblue')
window.title('Банк')


image = PhotoImage(file=r'D:\Разное\Игры и программы\Maximum\Module 2\Lesson 8\logo.png')
label_image = Label(window, image= image, bg='lightblue')
label_image.place(x=0,y=0)

label_title = Label(window, text='БАНК 2035', font='Arial 36', bg='lightblue')
label_title.place(x=200, y=50)

label_currency = Label(window, text=f'Курсы на {today}:', font='Arial 22', bg='lightblue')
label_currency.place(x=20,y=180)

dollar_info = f"{get_course('R01235').get('name')} {get_course('R01235').get('value')}"
dollar_label = Label(window, text=dollar_info, font='Arial 18', bg='lightblue')
dollar_label.place(x=40, y=220)

euro_info = f"{get_course('R01239').get('name')} {get_course('R01239').get('value')}"
euro_label = Label(window, text=euro_info, font='Arial 18', bg='lightblue')
euro_label.place(x=40, y=260)


yuan_info = f"{get_course('R01375').get('name')} {get_course('R01375').get('value')}"
yuan_label = Label(window, text= yuan_info, font='Arial 18', bg='lightblue')
yuan_label.place(x=40, y=300)

label1 = Label(bg='blue')
label1.place(width=500, height=10, x=0,y=0) 
label2 = Label(bg='blue')
label2.place(width=500, height=10, x=0,y=490) 

entry = Entry(font='Arial 22')
entry.place(x=40,y=400)

y = 40

def search():
    global y

    y += 40

    currency_id = entry.get()
    currency_info = get_course(currency_id)

    currency_name = currency_info.get('name')
    currency_value = currency_info.get('value')

    currency_str = f'{currency_name} {currency_value}'
    currency_label = Label(window, text=currency_str, font="Arial 18", bg='lightblue')
    currency_label.place(x=40, y=300 + y)


    


b = Button(text='Найти', command=search)
b.place(x=400,y=400)




window.mainloop()