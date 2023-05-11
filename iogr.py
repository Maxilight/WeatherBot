from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import requests

bot = Bot('6268419925:AAHTyaH4BNJh2LVW0Wvueq_2459G3NzLJkQ')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, """
Привет, я бот который позволит находить нужные товары в <b><a href="http:www.n-katalog.ru/">N Каталоге</a></b>
Для того чтобы я отправил тебе товар, введи в поле его название...""",
parse_mode="html", disable_web_page_preview=0)



@dp.message_handler(content_types=['text'])
async def parser(message: types.message):
    url = 'https://n-katalog.ru/category/mobilnye-telefony/list' + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    all_links = soup.find_all('div', class_= 'text' )
    for link in all_links:
        print(link["text"])






executor.start_polling(dp)
