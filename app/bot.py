import telebot
from telebot import types
from sqlalchemy import create_engine
import os

import random

from create_xlsx import create_file
from get_last_5 import get_last_5
from models import User, session_maker
from randomizers import random_date

bot = telebot.TeleBot('5926204518:AAHM3Mi4qapJ1vwES9RFoYlD4HzTrfIAWHU')
ENGINE = create_engine('sqlite:///sqlite.db')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Записать работника')
    bot.send_message(message.from_user.id, 'Вы в главном меню', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_fio(message):
    if message.text == 'Записать работника':
        bot.send_message(message.from_user.id, 'Введите ФИО работника: ')
        bot.register_next_step_handler(message, save_fio)

def save_fio(message):
    user = User(fio=message.text, datar=random_date(), id_role=random.randint(1, 2))
    with session_maker() as session:
        session.add(user)
        session.commit()
    if message.text:
        create_file()
        document = open(r'./app/hi.xlsx', 'rb')
        bot.send_document(message.from_user.id, document)
        document.close()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hi.xlsx')
        os.remove(path)

bot.polling(none_stop=True, interval=0)
