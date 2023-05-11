from telegram import Update
from telegram.ext import Updater, CommandHandler

def start(update: Update, context):
    update.message.reply_text('Привет! Я бот для поиска музыки и фильмов. Введите /music или /movies для поиска.')


def get_music(query):
    pass


def music(update: Update, context):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text('Введите название песни или исполнителя.')
        return
    songs = get_music(query)
    if not songs:
        update.message.reply_text('По вашему запросу ничего не найдено.')
        return
    for song in songs:
        update.message.reply_text(f'{song["title"]} - {song["artist"]}\n{song["duration"]}\n{song["link"]}')





def movies(update: Update, context):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text('Введите название фильма.')
        return
    movies = get_movies(query)
    if not movies:
        update.message.reply_text('По вашему запросу ничего не найдено.')
        return
    for movie in movies:
        update.message.reply_text(f'{movie["title"]} ({movie["year"]})\nРейтинг: {movie["rating"]}\n{movie["link"]}')

updater = Updater('6155906873:AAH6jVBmNhsOUQQYPx_a1lCtwjFMkizEMtc', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('music', music))
dispatcher.add_handler(CommandHandler('movies', movies))
updater.start_polling()
updater.idle()
