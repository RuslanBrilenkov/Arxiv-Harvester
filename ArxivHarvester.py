import urllib.request
import re
import numpy as np
import datetime
import pandas as pd

def Harvester():
	'''
	Sending a request to a website and getting a response.
	
	Then, saving it as a (.txt) file.
	'''
	try:
		url = 'https://arxiv.org/list/astro-ph/new'
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

		req = urllib.request.Request(url, headers = headers)
		resp = urllib.request.urlopen(req)
		respData = resp.read()

		# We do not need to print it now. Instead. let's save the website response as a .txt file
		#print(respData)

		with open('Arxiv_data.txt', "w") as file:
			file.write(str(respData))
			
	except Exception as e:
		print(e)
	return None

def SavingTitles():
	'''
	Reading saved (.txt) data of website response.
	Separating the titles from the text using regular expressions.
	Going through each paper title to get interesting papers by using 
	the numpy method intersect1d.
	'''
	try:
		with open("Arxiv_data.txt", "r") as file:
			Data = file.read()
		#print(Data)

		# separating the title names from the text
		titles = re.findall(r"Title:</span>(.*?)\\n</div>", Data)
		
		# Example key words of our interest
		My_keyWords = ['ALMA', 'dust', 'attenuation','IRX-beta', 'IRX', 'HST', '21cm']
		
		title_counter = 0
		TitlesToSave = []
		# going through each title and comparing with the key words of our interest
		for title in titles:
			# we split the words
			titleList = title.split(' ')
			
			# Checking the intersection between array of our key words and the selected titles
			# (in case there are more than 1 key word in the title, get the tite once)
			if (len(np.intersect1d(My_keyWords, titleList))>0):
				print("Found {keyword} in\n{title}\n".format(keyword=np.intersect1d(My_keyWords, titleList), title = title))
				TitlesToSave.append(str(title))
				title_counter += 1
		with open("Arxiv_data_titles.txt", "w") as file:
			file.write(str(TitlesToSave) )
		
		# printing a nice message for a user with a number of articles found
		if (title_counter==0):
			print("Unfortunately, I did not find any articles! Try to change the key words.")
		else:
			print("\nFound {} titles you might be interested in.\n".format(title_counter))
	
	except Exception as e:
		# in case the program fails at some point, see what is the reason
		print(e)
		pass
	
	return None

def SavingLinksAndTitles():
	'''
	This code read the Arxiv response and filters out infor about 
	paper title and the link to .pdf
	In return, saves a .txt file with this information.
	And prints out how many interesting papers found.
	
	Saved file as a name: 
	current daytime + number of papers found
	'''
	try:
		with open("Arxiv_data.txt", "r") as file:
			Data = file.read()
		
		# separating Links to papers and their titles
		LinkPlusTitle = re.findall(r"\<a href=\"\/abs\/(.*?)\".*?Title:</span> (.*?)\\n</div>", Data)
		
		# Example key words of our interest
		My_keyWords = ['ALMA', 'dust', 'attenuation','IRX-beta', 'IRX', 'HST', '21cm']
		
		title_counter = 0
		TitlesToSave = []
		LinksToSave = []
		for text in LinkPlusTitle:
			# we split the words
			titleList = text[1].split(' ')
			
			# Checking the intersection between array of our key words and the selected titles
			# (in case there are more than 1 key word in the title, get the tite once)
			if (len(np.intersect1d(My_keyWords, titleList))>0):
				# print title names if you wish:
				#print("Found {keyword} in\n{title}\n{link}\n".format(keyword=np.intersect1d(My_keyWords, titleList), title = text[1], link = "https://arxiv.org/pdf/"+text[0]+".pdf"))
				TitlesToSave.append(str(text[1]))
				LinksToSave.append(str("https://arxiv.org/pdf/"+text[0]+".pdf"))
				title_counter += 1
				
		
		extention = ".txt"
		currentDT = datetime.datetime.now()
		timeStr = str(currentDT.year)+"_"+str(currentDT.month)+"_"+str(currentDT.day)
		filenameToSave = timeStr+"_with_"+str(title_counter)+"_papers"+extention
		with open(filenameToSave, "w") as file:
			file.write(str(TitlesToSave) )
			file.write(str(LinksToSave) )
		
		# printing a nice message for a user with a number of articles found
		if (title_counter==0):
			print("Unfortunately, I did not find any articles! Try to change the key words.")
		else:
			print("\nFound {} titles you might be interested in.\n".format(title_counter))
	except Exception as e:
		print(e)
	
	return None

def UsingPands():
	pass

if (__name__=="__main__"):
	#Harvester()
	#SavingTitles()
	SavingLinksAndTitles()
	#PrintData()

