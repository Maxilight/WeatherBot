import telebot
bot = telebot.TeleBot('6155906873:AAH6jVBmNhsOUQQYPx_a1lCtwjFMkizEMtc')
import wikipedia
wikipedia.set_lang('ru')
from random import randint
'''
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler()
def get_text(message):
    if message.text == 'Привет' or message.text == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text == 'как дела?' or message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Норм')
    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать!')
#text = message.text




wikipedia.summary(quest, sentences=2)

@bot.message_handler()
def wiki(message):
    try:
        ask = wikipedia.summary(message.text, sentences=6)
    except:
        ask = 'Ошибка запроса...'
    bot.send_message(message.chat.id, ask)

@bot.message_handler()
def get_photo(message):
    if message.text == 'скинь картинку':
        photo = open('тимон.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['photo'])
def react(message):
    bot.send_message(message.chat.id, 'Клевая картинка!!!')

@bot.message_handler()
def wiki(message):
    index_image = randint(-1, 3)
    try:
        ask = wikipedia.summary(message.text, sentences=6)
    except:
        ask = 'Ошибка запроса...'
    bot.send_message(message.chat.id, ask)
    try:
        image = wikipedia.page(message.text).images[index_image]
        bot.send_photo(message.chat.id, image)
    except:
        bot.send_message(message.chat.id, 'image not found')


bot.polling(none_stop=True)
'''