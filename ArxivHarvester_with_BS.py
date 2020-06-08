#import pandas as pd
import requests
from bs4 import BeautifulSoup

def crawl():
	url = "https://arxiv.org/list/astro-ph/new"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	dlpage = soup.find_all(id='dlpage')
	
	dlist = dlpage[0].find('dl')
	
	dt = dlist.find_all('dt')
	dd = dlist.find_all('dd')
	
	for data in dd:
		title = data.find_all(class_="list-title mathjax")
		print(title)
	
	
	
if (__name__=="__main__"):
	crawl()
