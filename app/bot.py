import os
import logging
import random
import sys

import telebot
from telebot import types

import exceptions
from create_xlsx import create_file
from models import User, session_maker
from randomizers import random_date

# можно спрятать через dotenv
bot = telebot.TeleBot('5926204518:AAHM3Mi4qapJ1vwES9RFoYlD4HzTrfIAWHU')

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('Записать работника')
    try:
        bot.send_message(
            message.from_user.id, 'Вы в главном меню', reply_markup=keyboard
        )
        logger.info('сообщение отправлено')
    except exceptions.MessageSendError as error:
        logger.error(f'Не получается отправить сообщние: {error}')


@bot.message_handler(content_types=['text'])
def get_fio(message):
    if message.text == 'Записать работника':
        try:
            bot.send_message(message.from_user.id, 'Введите ФИО работника: ')
            logger.info('сообщение отправлено')
            bot.register_next_step_handler(message, save_fio)
        except exceptions.MessageSendError as error:
            logger.error(f'Не получается отправить сообщние: {error}')
    else:
        logger.error('Что-то идет не так')


def save_fio(message):
    try:
        user = User(
            fio=message.text, datar=random_date(), id_role=random.randint(1, 2)
        )
        with session_maker() as session:
            session.add(user)
            session.commit()
            logger.info('работник добавлен')
    except exceptions.CreateStaffError as error:
        logger.error(f'Не получается создать работника: {error}')
    if message.text:
        try:
            create_file()
            document = open(r'./app/staff.xlsx', 'rb')
            bot.send_document(message.from_user.id, document)
            logger.info('файл отправлен')
            document.close()
            path = os.path.join(
                os.path.abspath(os.path.dirname(__file__)), 'staff.xlsx'
            )
            os.remove(path)
        except exceptions.CreateFileError as error:
            logger.error(f'Не получается создать файл: {error}')
    else:
        logger.error('Что-то идет не так')


def main():
    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()
