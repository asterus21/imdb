import telebot
import random
import requests
from bs4 import BeautifulSoup

global text

def to_watch():

	films_list = []

	for pages in range(0, 10):
		pages = requests.get(f'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start={pages}01&ref_=adv_nxt')
		soup = BeautifulSoup(pages.text, 'lxml')
		films = soup.find_all('h3', class_='lister-item-header')
		movies = [film.a.text for film in films]
		films_list += movies

	text = films_list[random.randint(0, len(films_list) + 1)]
	return text

bot = telebot.TeleBot('here is your API key)

@bot.message_handler(commands=['start'])
def send_weclome(message):
	bot.reply_to(message, 'Hello!')

@bot.message_handler(commands=['film'])
def film_to_choose(message):
	bot.reply_to(message, 'Just a sec')
	bot.send_message(message.chat.id, to_watch())

@bot.message_handler(content_types=['text'])
def text_back(message):
	bot.reply_to(message, "Sorry, don't understand. Type /film to have a random one to watch.")

bot.polling()
