import speech_recognition as sr
from playsound import playsound #ЧТОБЫ ПРОИЗВЕСТИ ЗВУК
from gtts import gTTS
import os #ЧТОБЫ НАЙТИ ПУТЬ ФАЙЛОВ
import random

from tkinter import *

window = Tk()
window.geometry('800x800')
window.resizable(width=False,height=False)
window.config(bg='darkgrey')
window.title('Голосовой помощник Аврора')

image_path = os.path.abspath('Робот.png')
image = PhotoImage(file=image_path)


def menu():
    clear()
    label_image = Label(window, image= image, bg='darkgrey')
    label_image.place(x=200,y=100)

    welcome = Label(text= 'Пожалуйста, выберите функцию: Привет/Фильм/Музыка', font='Arial 18',bg='darkgrey')
    welcome.place(x=100,y=520)

    button = Button(text='Обратиться к помощнику', command=talking, bg='grey', font='Arial 12')
    button.place(width=200, height=50, x=300,y=630)


def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()
    

def talking():
    recognizer = sr.Recognizer()

    greetings = ['Доброго дня!', 'Здравствуйте!', 'И вам не хворать!']
    films = ['Время', '1+1', 'Побег из Шоушенка', 'Крёстный отец', 'Операция "Ы"']


    with sr.Microphone(device_index=1) as source:
        audio = recognizer.record(source, duration=3)
        speech = recognizer.recognize_google(audio, language='ru_RU')

        print(f'Вы сказали: {speech}') #ПРОВЕРКА СВЯЗИ
            

        if speech.lower() == 'фильм':
            menu()
            random_films = random.randrange(len(films))
            advice = Label(text = f'Советую вам посмотреть фильм "{films[random_films]}"!', font='Arial 18', bg='darkgrey')
            advice.place(x=100,y=570)
            converter = gTTS(text=f'Советую вам посмотреть фильм "{films[random_films]}"!', lang='ru')
            films = converter.save('films.mp3')
            path_film = os.path.abspath('films.mp3')
            playsound(path_film)

        if speech.lower() == "привет":
            menu()
            random_greeting = random.randrange(len(greetings))
            hello = Label(text = greetings[random_greeting], font='Arial 18', bg='darkgrey')
            hello.place(x=320,y=570)
            converter = gTTS(text= greetings[random_greeting], lang='ru')
            greetings = converter.save('greetings.mp3')
            path_greetings = os.path.abspath('greetings.mp3')
            playsound(path_greetings)
        

        if speech.lower() == 'музыка':
            menu()

            music = Label(text = f'Советую вам песню эту песню! Хотите послушать?', font='Arial 18', bg='darkgrey')
            music.place(x=100,y=570)

            converter = gTTS(text= f'Советую вам эту песню! Хотите послушать?', lang='ru')
            music = converter.save('music.mp3')
            path_music = os.path.abspath('music.mp3')
            playsound(path_music)
            


            def kish():
                playsound('Король и шут.mp3')
            button1 = Button(text='Король и шут', command=kish, bg='grey')
            button1.place(width=200,height=50,x=300,y=630)
            
            button2 = Button(text='Назад', command=menu,bg='grey')
            button2.place(width=200,height=50,x=300,y=690)
            

        if speech.lower() == 'мои 20-35':
            menu()
            yes_yes = Label(text='Все на месте', font='Arial 18', fg='red', bg='darkgrey')
            yes_yes.place(x=100, y=570)
            path_2023 = os.path.abspath('2023.mp3')   
            playsound(path_2023)

menu()

window.mainloop()
