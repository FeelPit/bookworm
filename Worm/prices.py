from bs4 import BeautifulSoup
from . import ser
from functools import lru_cache
import requests
import mysql.connector

def change(linking):
	i = 0
	shop_link = ''

	while i < len(linking):
		if i > 6:
			shop_link = shop_link + linking[i]
		else:
			pass
		i += 1
	return(shop_link)


@lru_cache(maxsize=100)
def take_prices_for_chitay_gorod(book):
		cnx = mysql.connector.connect(user='root', password='root',
	                            host='127.0.0.1',
	                            database='testik')
		cursor = cnx.cursor()
		book_true = ''
		for r in book:
			if r == ' ':
				r = '_'
				book_true += r
			else:
				book_true += r
		book_true1 = "'" + book_true + "'"
		if 1 == 2:
			cursor.execute("""
				SELECT price
				FROM testik.book
				WHERE name = {}""".format(book_true1))
			price_true = cursor.fetchall()
		else:	
			goog = 'https://www.google.ru/search?newwindow=1&ei=-UbzWauiOYTewALLt5PYCA&q='
			site = '+site%3Ahttps%3A%2F%2Fwww.chitai-gorod.ru&oq='
			site1 = '+site%3Ahttps%3A%2F%2Fwww.chitai-gorod.ru&gs_l=psy-ab.3...108217.111050.0.111227.10.8.2.0.0.0.158.938.3j5.8.0....0...1.1.64.psy-ab..0.0.0....0.Aa4oF7etZ-U'
			link = goog + book + site + book + site1

			req =  requests.get(link)
			soup = BeautifulSoup(req.text, 'html.parser')
			firts_link = soup.find('h3', attrs = {'class':'r'})
			
			for shop in firts_link.find_all('a'):
				shop_false = shop.get('href')

			shop_true = change(shop_false)
			
			req_shop_link = requests.get(shop_true)
			soup_shop_link = BeautifulSoup(req_shop_link.text, 'html.parser')
			print(soup_shop_link)
			price = soup_shop_link.find('div', attrs = {'class':'product-price'})
			print(price)
			price_false = price.get_text()
			price_true = ''
			for p in price_false:
				if p == price_false[-1] or p == price_false[-2]:
					pass
				else:
					price_true += p
			return(price_true)

'''@lru_cache(maxsize=100)
def take_prices_for_labirint(book):
		cnx = mysql.connector.connect(user='root', password='root',
	                            host='127.0.0.1',
	                            database='testik')
		cursor = cnx.cursor()
		book_true = ''
		for r in book:
			if r == ' ':
				r = '_'
				book_true += r
			else:
				book_true += r
		book_true1 = "'" + book_true + "'"
		if 1 == 2:
			cursor.execute("""
				SELECT price
				FROM testik.book
				WHERE name = {}""".format(book_true1))
			price_true = cursor.fetchall()
		else:
			goog = 'https://www.google.ru/search?newwindow=1&ei=akfzWeuAFNCkwQLe-r7QDg&q='
			site = '+site%3Ahttps%3A%2F%2Fwww.labirint.ru%2F&oq='
			site1 = '+site%3Ahttps%3A%2F%2Fwww.labirint.ru%2F&gs_l=psy-ab.3...6558256.6558256.0.6559183.1.1.0.0.0.0.96.96.1.1.0....0...1.2.64.psy-ab..0.0.0....0.ylcsp3bO_bI'
			link = goog + book + site + book + site1


			req = requests.get(link)
			soup = BeautifulSoup(req.text, 'html.parser')
			firts_link = soup.find('h3', attrs = {'class': 'r'})


			for shop in firts_link.find_all('a'):
				shop_false = shop.get('href')


			shop_true = change(shop_false)


			req = requests.get(shop_true)
			soup_shop_link = BeautifulSoup(req.text, 'html.parser')
			price = soup_shop_link.find('span', attrs = {'class':'buying-price-val-number'})
			price_new = soup_shop_link.find('span', attrs = {'class':'buying-pricenew-val-number'})
			if price == None:
				return(price_new.get_text())
			else:
				return(price.get_text())
'''
def comprasion(fir, sec):
		if int(fir) > int(sec):
			return(sec)
		elif int(sec) < int(fir):
			return(fir)
		else:
			return(fir)	
#v = take_prices_for_chitay_gorod('Стив Джобс')
v1 = take_prices_for_labirint('Война и мир')