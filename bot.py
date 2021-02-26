import telebot
import random
import requests
from bs4 import BeautifulSoup
global text

bot = telebot.TeleBot('1488537036:AAEc1bcx7dCSP4m1XXwTN_6sfg_uli9Tkfk')

def film_to_watch():

	films_list = []

	for pages in range(0, 10):
		pages = requests.get(f'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start={pages}01&ref_=adv_nxt')
		soup = BeautifulSoup(pages.text, 'lxml')
		films = soup.find_all('h3', class_ = 'lister-item-header')
		movies = [film.a.text for film in films]
		films_list += movies

	text = str(print(films_list[random.randint(0, len(films_list) + 1)]))
	return text

@bot.message_handler(commands=['start'])
def send_weclome(message):
	bot.reply_to(message, 'Hello!')

@bot.message_handler(commands=['film'])
def answer(message):
	bot.send_message(message, film_to_watch())

@bot.message_handler(content_types=['text'])
def text_back(message):
	bot.reply_to(message, "Sorry, don't understand. Type /film to have a random one to watch.")

bot.polling()