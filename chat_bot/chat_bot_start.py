import telebot
from telebot import types
from googletrans import Translator
from langdetect import detect
import sqlite3


API_TOKEN = '6028101102:AAFeWXaKdb9txqyVVbglcGQVRnQOCTVr_MM'

bot = telebot.TeleBot(API_TOKEN)


translator = Translator()


@bot.message_handler(commands=['start'])
def started(mess):
    """Начальные кнопки после запуска бота и переход к следующему шагу"""
    button = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти к разделам!')
    btn2 = types.KeyboardButton('Интересная книга на английском')
    button.add(btn1)
    button.add(btn2)
    bot.send_message(mess.chat.id, f'{mess.from_user.first_name}, добро пожаловать в обучающий бот!\n'
                                   f'', reply_markup=button)
    bot.register_next_step_handler(mess, step_one)
    bot.register_next_step_handler(mess, book)


@bot.message_handler(commands=['site, website'])
def book(mess):
    """Функция для отправки ссылки в чат"""
    if mess.text == 'Интересная книга на английском':
        bot.send_message(mess.chat.id, 'https://2books.su/books/peter-pan-j-m-barrie/')


@bot.message_handler(commands=['button'])
def step_one(mess):
    """Создание кнопок и переход к следующему шагу"""
    button = types.ReplyKeyboardMarkup()
    btn3 = types.KeyboardButton('Английский алфавит с произношением')
    btn5 = types.KeyboardButton('Перевести слово')
    btn6 = types.KeyboardButton('Выбери правильный вариант')
    button.add(btn3)
    button.add(btn5)
    button.add(btn6)
    bot.send_message(mess.chat.id, 'Чем хотите заняться?', reply_markup=button)
    bot.register_next_step_handler(mess, step_two)


def step_two(mess):
    """Обработка выбранных пользователем кнопок и выполнение действий по ним"""
    if mess.text == 'Английский алфавит с произношением':
        bot.send_message(mess.chat.id, 'Вы выбрали алфавит!')
        file = open('../../Test/chat_bot/Alphabet.jpg', 'rb')
        bot.send_photo(mess.chat.id, file)
        bot.register_next_step_handler(mess, step_two)
    elif mess.text == 'Перевести слово':
        bot.send_message(mess.chat.id, 'Пожалуйста, введите слово, фразу или предложение на английском.\n'
                                       'Если хотите закончить с переводом - введите stop')
        bot.register_next_step_handler(mess, translate_message)
    elif mess.text == 'Выбери правильный вариант':
        bot.send_message(mess.chat.id, 'Перейдем к тесту')
        bot.register_next_step_handler(mess, start_testing)


@bot.message_handler(func=lambda m: True)
def translate_message(mess):
    """Функция для перевода текста"""
    if mess.text.lower() == 'stop':
        bot.send_message(mess.chat.id, 'Завершаем перевод')
        return bot.register_next_step_handler(mess, step_two)
    src = detect(mess.text.lower())
    dest = 'ru'
    translated_text = translator.translate(mess.text, src=src, dest=dest).text
    bot.send_message(mess.chat.id, translated_text)


@bot.message_handler(commands=['text'])
def start_testing(mess):
    """Функция вывода вопроса для пользователя"""
    connection = sqlite3.Connection('my_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Testing')
    question = cursor.fetchall()

    cursor.close()
    connection.close()
    bot.send_message(mess.chat.id, f'Вопрос № {question[0][1]}')
    bot.register_next_step_handler(mess, next_question)


@bot.message_handler(func=lambda m: True)
def next_question(mess):
    """Функция вывода ответов для пользователя"""
    connection = sqlite3.Connection('my_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Testing')
    question = cursor.fetchall()

    cursor.close()
    connection.close()
    bot.send_message(mess.chat.id, f'Вопрос № {question[0][1]}')

    button = types.ReplyKeyboardMarkup()
    btnA = types.KeyboardButton(f'{question[0][2]}')
    btnB = types.KeyboardButton(f'{question[0][3]}')
    btnC = types.KeyboardButton(f'{question[0][4]}')
    button.add(btnA)
    button.add(btnB)
    button.add(btnC)
    bot.send_message(mess.chat.id, 'Выберите правильный ответ', reply_markup=button)
    bot.register_next_step_handler(mess, get_amswer)


def get_amswer(mess):
    my_lst = []
    connection = sqlite3.Connection('my_database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Testing')
    question = cursor.fetchall()

    cursor.close()
    connection.close()

    if mess.text == f'{question[0][2]}':
        bot.send_message(mess.chat.id, 'Не правильно!')
    elif mess.text == f'{question[0][3]}':
        bot.send_message(mess.chat.id, 'Не правильно!')
    elif mess.text == f'{question[0][3]}':
        bot.send_message(mess.chat.id, 'Верный ответ!')


bot.polling(none_stop=True)
