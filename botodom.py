import requests
from bs4 import BeautifulSoup as b
import random
import telebot
URL = "https://www.anekdot.ru/last/good/"
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_nekdo = parser(URL)
random.shuffle(list_of_nekdo)

bot = telebot.TeleBot('6075712406:AAGntMyihOztaQ2oXv2ba4R7YBQd3Oc_3sY')
@bot.message_handler(commands=['Привет'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для поиска анекдотов, музыки и фильмов. Введите /music или /movies для поиска.')
@bot.message_handler(content_types='text')
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_nekdo[0])
        del list_of_nekdo
    else:
        bot.send_message(message.chat.id, 'Привет, увидеть анекдот нажимаем любую цифру:')
bot.polling(none_stop=True)









