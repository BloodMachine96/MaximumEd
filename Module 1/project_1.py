from tkinter import *
from bs4 import BeautifulSoup
import random
import requests
import webbrowser #Импортируем эту библиотеку для того, чтобы позже создать нажимаемую ссылку.
from fpdf import FPDF
from datetime import datetime


#Создаём окно.
window = Tk()
window.geometry('700x600')
window.title('Fest_chooser v1.0')

#Создаём меню. Оборачиваем в функцию, чтобы можно было вызывать её с помощью кнопки.
def menu():
    clear()
    label_title = Label(text='Желаете найти фестеваль?',font=('Arial', 24), fg='white', bg='green')
    label_title.place(width=700, height=50, x=0, y=0)

    label_2 = Label(bg='green')
    label_2.place(width=700, height=50, x=0, y=550)

    label_3 = Label(text='Смотрите также...',bg='green', fg='white', font=('Arial', 24))
    label_3.place(width=700, height=50, x=0, y=350)

    b_1 = Button(text='Найти фестиваль', font=('Arial', 18),bg='green', fg='white', command=parse)
    b_1.place(x=255, y=150)

    b_2 = Button(text='Антистресс', font=('Arial', 18), bg='green', fg='white', command=clicker)
    b_2.place(x=85, y=450, width=250)

    b_3 = Button(text='Открытка', font=('Arial', 18), bg='green', fg='white', command=postcard)
    b_3.place(x=385, y=450, width=250)


#Создаём вспомогательные функции.
def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()

def back_to_menu():
    b = Button(text='Меню', font=('Arial', 16), fg='black', command=menu) 
    b.place(x=25, y=500, width=100)

#Делаем адскую аджику(парсим)
def parse():
    clear()
    back_to_menu()

    label_upper = Label(bg='green')
    label_upper.place(width=700, height=50, x=0, y=0)

    label_down = Label(bg='green')
    label_down.place(width=700, height=50, x=0, y=550)

    # Первый фестиваль
    response = requests.get("https://kudago.com/msk/festival/")
    soup = BeautifulSoup(response.text, "html.parser")
    fest1 = random.choice(soup.find_all(class_="post-title-link"))
    link1 = fest1['href']

    def callback(event):
        webbrowser.open_new(link1)

    fest_lable1 = Label(text=fest1['title'], bg='green', fg='white', font=('Arial', 15))
    fest_lable1.place(width=700, x=0, y=50)

    fest_link1 = Label(text=fest1['href'], fg='blue', cursor='hand2', font=('Arial', 12))
    fest_link1.pack()
    fest_link1.bind("<Button-1>", callback)
    fest_link1.place(x=50, y=100)

    # Второй фестиваль
    fest2 = random.choice(soup.find_all(class_="post-title-link"))
    link2 = fest2['href']

    def callback(event):
        webbrowser.open_new(link2)

    fest_lable2 = Label(text=fest2['title'], bg='green', fg='white', font=('Arial', 15))
    fest_lable2.place(width=700, x=0, y=150)
    
    fest_link2 = Label(text=fest2['href'], fg='blue', cursor='hand2', font=('Arial', 12))
    fest_link2.pack()
    fest_link2.bind("<Button-1>", callback)
    fest_link2.place(x=50, y=200)

    # Третий фестиваль
    fest3 = random.choice(soup.find_all(class_="post-title-link"))
    link3 = fest3['href']

    def callback(event):
        webbrowser.open_new(link3)

    fest_label3 = Label(text=fest3['title'], bg='green', fg='white', font=('Arial', 15))
    fest_label3.place(width=700, x=0, y=250)
    
    fest_link3 = Label(text=fest3['href'], fg='blue', cursor='hand2', font=('Arial', 12))
    fest_link3.pack()
    fest_link3.bind("<Button-1>", callback)
    fest_link3.place(x=50, y=300)

    reset_button = Button(text='Случайные', font=('Arial', 16), fg='black', command=parse)
    reset_button.place(x=140, y=500, width=150) #Случайные фестивали 

#Антистресс в виде кликера
def clicker():
    clear()
    back_to_menu()
    global points, bg_index
    bg_values = ['black', 'blue', 'red', 'pink', 'green']
    points = 0
    bg_index = 0

    def check():
        global points, bg_index
        points += 1
        label['text'] = points
        b_3.place(x=random.randint(1, 550), y=random.randint(1, 350))
        if points % 20 == 0:
            bg_index = 0 if bg_index == len(bg_values) else bg_index + 1
            b_3['bg'] = bg_values[bg_index]
            b_3['fg'] = 'white'
    
    b_3 = Button(text='Нажми меня', font=('Arial', 20), fg='black', command=check)
    b_3.place(x=350, y=300)
    label = Label(text=points, font=('Arial', 15), fg='black')
    label.place(x=10, y=10)


#Создание открытки
def postcard():
    clear()
    back_to_menu()

    label_postcard = Label(text='Введите необходимые ответы в консоль',bg='green', fg='white',font=('Arial', 18))
    label_postcard.place(width=700, height=50, x=0, y=0)

    pdf = FPDF('P','mm', 'A4')
    pdf.add_page()
    pdf.set_right_margin(50)
    pdf.set_left_margin(50)

    pdf.image('bg.jpg', w=210, h=297, x=0, y=0)
    pdf.add_font('comic', '', 'C:\WINDOWS\FONTS\COMIC.ttf', uni=True)
    pdf.set_font('comic', size=18)

    bg=input('На какую тематику будет открытка? День рождение/другу/маме: ')
    pol=input('Какого пола получатель? Введите м/ж: ')
    name=input('Как зовут получателя? ')
    text=input('Введите текст поздравления: ')
    pdf.set_text_color(0, 0, 0)


    if bg == 'день рождение':
        pdf.image('bg.jpg', w=210, h=297, x=0, y=0)
    elif bg == 'другу':
        pdf.image('bg4.jpg', w=210, h=297, x=0, y=0)
    elif bg == 'маме':
        pdf.image('bg5.jpg', w=210, h=297, x=0, y=0)
    else:
        print('Не выбрана тематика открытки!')
        raise SystemExit

    if pol == 'м':
        pdf.cell(w=0,h =90, ln=1)
        pdf.cell(w=0, h=20, txt='Дорогой, ' + name + '!', align='C', ln=1)
    elif pol == 'ж':
        pdf.cell(w=0,h =90, ln=1)
        pdf.cell(w=0, h=20, txt='Дорогая, ' + name + '!', align='C', ln=1)
    else: 
        print('Не выбран пол получателя!')
        raise SystemExit
    pdf.multi_cell(w=0, h=15, txt=text, align='C')

    today = datetime.today().strftime('%d/%m/%Y')
    pdf.cell(w=0, h=25, txt=today, align='R')

    from_ = input('От кого открытка? ')
    pdf.cell(w=0, h=40, txt=from_, align='R')


    pdf.output('postcard.pdf')

menu()


window.mainloop()