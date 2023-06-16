from gtts import gTTS

my_file = open("test.txt", "r", encoding='utf-8') #'w'

my_str = my_file.read()

my_file.close()

converter = gTTS(text=my_str, lang='en')#в файле меняешь текст на рус и здесь 'en' на 'ru'

converter.save("test.mp3")

print(my_str)