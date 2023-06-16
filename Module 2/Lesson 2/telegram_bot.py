from telebot import TeleBot
from telebot.types import (Message,
 ReplyKeyboardMarkup,
 KeyboardButton,
  InlineKeyboardMarkup,
    InlineKeyboardButton)
import random

bot = TeleBot('5935443225:AAFopji5naIjax31YYPpCsH1Sn1MBMfMgBk')
BASE_FILES_DIR = 'D:\Разное\Игры и программы\Maximum\Module 2\Lesson 2\extra'

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
    button5 = KeyboardButton('/tip_game')

    keyboard.add(button1, button2, button3, button4, button5)
    return keyboard

@bot.message_handler(commands=['cats'])
def cats(message: Message):
    random_img_number = random.randint(1, 9)
    random_img = open(fr'{BASE_FILES_DIR}\{random_img_number}.jpg', 'rb')
    bot.send_photo(message.from_user.id, random_img)

@bot.message_handler(commands=['music'])
def music(message: Message):
    audio = open(fr'{BASE_FILES_DIR}\happy.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)

@bot.message_handler(commands=['poem'])
def poem(message: Message):
    bot.send_message(message.from_user.id, 
    'Села муха на варенье, вот и всё стихотворенье!')
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text='Перейти', url='https://stihi.ru/')
    keyboard.add(button)
    bot.send_message(message.from_user.id, 'Больше стихотворений здесь:', reply_markup=keyboard)

@bot.message_handler(commands=['sticker'])
def sticker(message: Message):
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEG-AJjpcr08flQC8hkyqyliEYzRaT3XQAC4CEAAn-2KEkXVoibL2ZWZywE')


@bot.message_handler(commands=['tip_game'])
def tip_game(message: Message):
    bot.send_message(message.from_user.id, 'Привет!')

    keyboard2 = ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)

    button_a = KeyboardButton(text = '/action')
    button_b = KeyboardButton(text = '/roleplay')
    button_c = KeyboardButton(text = '/strategy')
    button_d = KeyboardButton(text = '/simulators')
    button_e = KeyboardButton(text = '/adventure')
    button_f = KeyboardButton(text = '/golovolomki')
    keyboard2.add(button_a, button_b, button_c, button_d, button_e, button_f)

    bot.send_message(message.from_user.id, 'Какой игровой жанр вы предпочитаете?', reply_markup=keyboard2)

    return keyboard2

@bot.message_handler(commands=['action'])
def action(message: Message):
    bot.send_message(message.from_user.id, 'Советую поиграть в The Elder Scrolls V: Skyrim')

@bot.message_handler(commands=['roleplay'])
def roleplay(message: Message):
    bot.send_message(message.from_user.id, 'Советую поиграть в The Elder Scrolls V: Skyrim')

@bot.message_handler(commands=['strategy'])
def strategy(message: Message):
    bot.send_message(message.from_user.id, 'Советую поиграть в The Elder Scrolls V: Skyrim')

@bot.message_handler(commands=['simulators'])
def simulators(message: Message):
    bot.send_message(message.from_user.id, 'Советую поиграть в The Elder Scrolls V: Skyrim')

@bot.message_handler(commands=['adventure'])
def adventure(message: Message):
    bot.send_message(message.from_user.id, 'Советую поиграть в The Elder Scrolls V: Skyrim')

@bot.message_handler(commands=['golovolomki'])
def golovolomki(message: Message):
    bot.send_message(message.from_user.id, 'Советую поиграть в The Elder Scrolls V: Skyrim')

bot.polling()