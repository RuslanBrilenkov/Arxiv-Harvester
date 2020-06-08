import requests
from bs4 import BeautifulSoup
import numpy as np
from tqdm.auto import tqdm # for a progress bar
#import pandas as pd

def crawl():
	url = "https://arxiv.org/list/astro-ph/new"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	dlpage = soup.find_all(id='dlpage')
	
	dlist = dlpage[0].find('dl')
	
	dt = dlist.find_all('dt')
	dd = dlist.find_all('dd')

	# Example key words of our interest
	My_keyWords = ['ALMA', 'dust', 'attenuation','IRX-beta', 'IRX', 'HST']

	title_counter = 0
	TitlesToSave = []
	LinksToSave = []

	for data in tqdm(dd):
		
		title = data.find_all(class_="list-title mathjax")
		# separate titles for words:
		title_words = str(title[0]).split(' ')
		
		# looking for coincidences in key words
		# (in case there are more than 1 key word in the title, get the title only once)
		if (len(np.intersect1d(My_keyWords, title_words))>0):
			# print title names if you wish:
			print("Found {keyword} in\n{title}\n".format(keyword=np.intersect1d(My_keyWords, title_words), title = title))#, link = "https://arxiv.org/pdf/"+text[0]+".pdf"))
			TitlesToSave.append(title)
	#         LinksToSave.append(str("https://arxiv.org/pdf/"+text[0]+".pdf"))
			title_counter += 1
			
	# printing a nice message for a user with a number of articles found
	if (title_counter==0):
		print("Unfortunately, I did not find any articles! Try to change the key words.")
	else:
		print("\nFound {} title(s) you might be interested in.\n".format(title_counter))
	
	
if (__name__=="__main__"):
	crawl()
