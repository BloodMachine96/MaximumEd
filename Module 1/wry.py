# import requests
# from bs4 import BeautifulSoup
# import random

# response = requests.get('https://i-fakt.ru/')
# soup = BeautifulSoup()
# facts = soup.find_all(class_='p-2 clearfix')
# for i_fact in facts:
#     print(i_fact.h4)
#     print(i_fact.a['href'])
#     print('--' * 100)

# pip install requests
# p-2 clearfix
# https://i-fakt.ru/
# pip3
# pip install bs4

# import requests
# from bs4 import BeautifulSoup
# import random

# response = requests.get('https://kudago.com/msk/festival/')
# soup = BeautifulSoup(response.text, 'html.parser')
# fest = random.choice(soup.find_all(class_='post-title-link'))
# print(fest['href'])
# print(fest['title'])

# https://kudago.com/msk/festival/
# post-title-link

# var = IntVar
#     Choice1 = Radiobutton(text='День рождение', variable=var, value=1)
#     Choice1.place(x=10, y=100)
#     Choice2 = Radiobutton(text='Другу', variable=var, value=2)
#     Choice2.place(x=10, y=150)
#     Choice3 = Radiobutton(text='Маме', variable=var, value=3)
#     Choice3.place(x=10, y=200)
#     Answer = Button(text='Ответить', command=Theme)
#     Answer.place(x=10, y=250)

#     def Theme():
#         clear()
#         back_to_menu()
#         Theme_choice = var.get()
#         if Theme_choice == 1:
#             pdf.image('bg.jpg', w=210, h=297, x=0, y=0)
#         elif Theme_choice == 2:
#             pdf.image('bg4.jpg', w=210, h=297, x=0, y=0)
#         elif Theme_choice == 3:
#             pdf.image('bg5.jpg', w=210, h=297, x=0, y=0)
#         NameAnswer()

#     def NameAnswer():
#         message = StringVar()
#         message_entry = Entry(textvariable=message)
#         message_entry.place(x=10, y=450)
#         message_button = Button(text="Выберите статью", command=Name)
#         message_button.place(x=1100, y=600, anchor="c")
#         def Name():
#             global name
#             clear()
#             back_to_menu()
#             name = str(message.get())
#             PolAnswer()

#     var2 = IntVar

#     def PolAnswer():
#         global PolChoice1, PolChoice2, Answer2
#         PolChoice1 = Radiobutton(text='Женский', variable=var2, value=5)
#         PolChoice2 = Radiobutton(text='Мужской', variable=var2, value=6)
#         Answer2 = Button(text='Ответить', fg='black', font=('Arial', 18), width=50, command=male_or_female)
#         def male_or_female():
#             clear()
#             back_to_menu()
#             male_or_female_choice = var2.get()
#             if male_or_female_choice == 5:
#                 pdf.cell(w=0,h =90, ln=1)
#                 pdf.cell(w=0, h=20, txt='Дорогой, ' + name + '!', align='C', ln=1)
#             if male_or_female_choice == 6:
#                 pdf.cell(w=0,h =90, ln=1)
#                 pdf.cell(w=0, h=20, txt='Дорогая, ' + name + '!', align='C', ln=1)
#             TextAnswer()
    
#     def TextAnswer():
#         message2 = StringVar()
#         message_entry2 = Entry(textvariable=message2)
#         message_entry2.place(x=10, y=450)
#         message_button2 = Button(text="Выберите статью", command=Name)
#         message_button2.place(x=1100, y=600, anchor="c")
#         def Name():
#             global text
#             clear()
#             back_to_menu()
#             text = str(message2.get())
#             PolAnswer()


#     pdf.multi_cell(w=0, h=15, txt=text, align='C')

#     today = datetime.today().strftime('%d/%m/%Y')
#     pdf.cell(w=0, h=25, txt=today, align='R')

#     from_ = input('От кого открытка? ')
#     pdf.cell(w=0, h=40, txt=from_, align='R')
    

#     pdf.output('postcard.pdf')

import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)