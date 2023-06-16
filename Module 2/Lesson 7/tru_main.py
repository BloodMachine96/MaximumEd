import speech_recognition as sr
import random


recognizer = sr.Recognizer()


greetings = ['И тебе привет!', 'Здравствуй!', 'И тебе нехворать!']
films = ['Кот в сапогах 2: Последнее желание', '1+1', 'Побег из Шоушенка', 'Крёстный отец', 'Операция "Ы"']

while True:
    with sr.Microphone(device_index=1) as source:
        print('Пожалуйста, выберите функцию: Привет/Фильм')
        audio = recognizer.listen(source)

        speech = recognizer.recognize_google(audio, language='ru_RU')

        print(f'Вы сказали: {speech}')

        if speech.lower() == "привет":
            random_greetings = random.randrange(len(greetings))
            print(greetings[random_greetings])

        if speech.lower() == 'фильм':
            random_films = random.randrange(len(films))
            print(f'Советую вам посмотреть "{films[random_films]}"!')



# from datetime import datetime

# today = datetime.today()
# today = today.strftime('%d/%m/%Y')

# print(today)