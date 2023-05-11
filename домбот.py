import telebot
import requests
from bs4 import BeautifulSoup
from random import randint, choice

'''
random_page = randint(1, 1600)
url = f'https://nekdo.ru/short/{random_page}'
r = requests.get(url)
#print(r.text)
soup = BeautifulSoup (r.text, 'html.parser')
all_anek = soup.find_all('div', class_ = 'text')
#print(all_anek)
clear_anek = []
for i in all_anek:
    clear_anek.append(i.getText())
#print(clear_anek)
random_anekdot = choice(clear_anek)
#print(random_anekdot)
bot = telebot.TeleBot('6222015930:AAFXgUZjbLvSki0ZLqBe--dfRH8raBeoWkw')
image_list = ['image/1.jpg','image/2.jpg','image/3.jpg','image/4.jpg','image/5.jpg','image/6.jpg','image/7.jpg','image/8.jpg','image/9.jpg','image/10.jpg','image/11.jpg','image/12.jpg','image/13.jpg']
def start(message):
    bot.send_message(message.chat.id, 'Привет, я расскажу тебе анекдот и скину картинки')

@bot.message_handler(content_types='text')
def anekdot(message):
    if message.text == 'повесели меня':
        random_anekdot = choice(clear_anek)
        bot.send_message(message.chat.id, random_anekdot )
    elif message.text == 'скинь картинку':
        random_image = choice(image_list)
        image = open(random_image, 'rb')
        bot.send_photo(message.chat.id, image)

from telebot import types
bot = telebot.TeleBot('6222015930:AAFXgUZjbLvSki0ZLqBe--dfRH8raBeoWkw')
@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    kb_dog = types.InlineKeyboardButton(text='собачка', callback_data='dog')
    kb_cat = types.InlineKeyboardButton(text='кошечка', callback_data='cat')
    kb.add(kb_dog, kb_cat)
    bot.send_message(message.chat.id, 'Выбери себе животное: ', reply_markup=kb )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'dog':
        kb_dog = types.InlineKeyboardMarkup()
        kb_dog_w = types.InlineKeyboardButton(text='белого цвета', callback_data='white')
        kb_dog_b = types.InlineKeyboardButton(text='черного цвета', callback_data='black')
        kb_dog.add(kb_dog_w, kb_dog_b)
        bot.send_message(call.message.chat.id, 'Какого цвета? : ', reply_markup=kb_dog)
    elif call.data == 'cat':
        kb_cat = types.InlineKeyboardMarkup()
        kb_cat_w = types.InlineKeyboardButton(text='белого цвета', callback_data='white')
        kb_cat_b = types.InlineKeyboardButton(text='черного цвета', callback_data='black')
        kb_cat.add(kb_cat_w, kb_cat_b)
        bot.send_message(call.message.chat.id, 'Какого цвета? : ', reply_markup=kb_cat)
'''
bot = telebot.TeleBot('6222015930:AAFXgUZjbLvSki0ZLqBe--dfRH8raBeoWkw')
@bot.message_handler()
def inputa(message):
    in_telega = message.text
    if in_telega.isdigit():
        print('yes')
        in_telega = int(in_telega)
        in_telega *= 0.62
    bot.send_message(message.chat.id, in_telega)


bot.polling(none_stop=True)