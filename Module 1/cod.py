# # try:
# #     name = input('Как вас зовут? ')
# #     age = int(input('Сколько вам лет? '))

# # except ValueError:
# #     print('Некорректный возраст.')



# # else:
# #     print('Привет, {name} , тебе {age} лет!'.format(name=name, age=age))
# #     print('Привет, {} , тебе {} лет!'.format(name, age))
# #     print(f'Привет, {name} , тебе {age} лет!')

# # finally:
# #     print('Программа отработала.')

# # numbers = [5, 4, 2, 1, 7, 9, 8, 6, 4]

# # print(numbers[5:2:-1])

# # print(numbers[::-1])

# def summa(a, b):
#     print(a + b)

# result = summa(100 + 5)

from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

bot = TeleBot('5935443225:AAFopji5naIjax31YYPpCsH1Sn1MBMfMgBk')


@bot.message_handler(commands=['start', 'help'])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, 'Привет! Выбери следующие команды:', reply_markup=keyboard)


def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    button1 = KeyboardButton('/cats')
    button2 = KeyboardButton('/poem')
    button3 = KeyboardButton('/sticker')
    button4 = KeyboardButton('/music')

    keyboard.add(button1, button2, button3, button4)
    return keyboard


bot.polling()
