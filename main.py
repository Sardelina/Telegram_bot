import telebot
import random
from telebot import types

token = '2130527377:AAEfvP9z1mkC61g2pKnEykJ9a7dvhcP8n-c'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу",'Как дела?','Музыка','Картинка', "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу отправить вам свои любимые песни, одну смешную картинку, можете узнать где я учусь, а также спросить как у меня дела.')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == 'как дела?':
        if random.randint(1,2) == 1:
            bot.send_message(message.chat.id, 'Отлично!')
        else:
            bot.send_message(message.chat.id, 'Да как-то не очень...')
    elif message.text.lower() == "музыка":
        if random.randint(1,3) == 1:
            bot.send_message(message.chat.id, 'Конечно, послушай – https://www.youtube.com/watch?v=nj6YamxIv4o')
        if random.randint(1,3) == 2:
            bot.send_message(message.chat.id, 'Конечно, послушай – https://www.youtube.com/watch?v=rPMvuHRao00')
        if random.randint(1,3) == 3:
            bot.send_message(message.chat.id, 'Конечно, послушай – https://www.youtube.com/watch?v=fr0-hZXqzOU')
    elif message.text.lower() == "картинка":
        bot.send_message(message.chat.id, 'Конечно, посмотри – https://forum.funline.pw/data/avatars/l/0/100.jpg?1631896126')

bot.polling(none_stop=True)