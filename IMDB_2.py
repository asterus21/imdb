import random
import requests
from bs4 import BeautifulSoup

def film_to_watch():

	films_list = []

	for pages in range(0, 10):
		pages = requests.get(f'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start={pages}01&ref_=adv_nxt')
		soup = BeautifulSoup(pages.text, 'lxml')
		films = soup.find_all('h3', class_ = 'lister-item-header')
		movies = [film.a.text for film in films]
		films_list += movies

	#print(pages.status_code)
	#print(len(films_list))

	random_film = print(films_list[random.randint(0, len(films_list) + 1)])

	return random_film

film_to_watch()