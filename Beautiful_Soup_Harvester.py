import requests
from bs4 import BeautifulSoup
import numpy as np
from tqdm.auto import tqdm # for a progress bar
import re

def crawl():
    url = "https://arxiv.org/list/astro-ph/recent"
    url = "https://arxiv.org/list/astro-ph/new?skip=0&show=1000"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    dlpage = soup.find_all(id='dlpage')

    dlist = dlpage[0].find('dl')

    dt = dlist.find_all('dt')
    dd = dlist.find_all('dd')

    # Example key words of our interest
    My_keyWords = ['ALMA', 'dust', 'attenuation','IRX-beta', 'IRX', 'HST', "VLA", "Parity"]

    # Mayb or may not use it -> if you want to sve the results locally 
    title_counter = 0
    TitlesToSave = []
    LinksToSave = []

    # Creatting an array of links to papers - using regular expressions (re)
    Links = []
    for T in dt:
        links = T.find_all('a', title='Download PDF')
        link = re.findall(r"href\=\"(.*?)\"", str(links) )
        Links.append(link)

    # now, separating titles and looking for interesting ones
    indx = 0
    for data in tqdm(dd):

        title = data.find_all(class_="list-title mathjax")
        title_to_string = str(title).split("</span>")[1][:-7] # to crop the last bit: "</div>]"
        #print(title_to_string) 
        # separate titles for words:
        title_words = title_to_string.split(' ')

        # looking for coincidences in key words
        # (in case there are more than 1 key word in the title, get the title only once)
        if (len(np.intersect1d(My_keyWords, title_words))>0):
            # print title names if you wish:
            print("Found {keyword} in\n{title}\n".format(keyword=np.intersect1d(My_keyWords, title_words), title = title_to_string))#, link = "https://arxiv.org/pdf/"+text[0]+".pdf"))
            TitlesToSave.append(title_to_string)
    #         LinksToSave.append(str("https://arxiv.org/pdf/"+text[0]+".pdf"))
            title_counter += 1

            LinksToSave.append("https://arxiv.org"+str(Links[indx][0]) )
        indx +=1

    # printing a nice message for a user with a number of articles found
    if (title_counter==0):
        print("Unfortunately, I did not find any articles! Try to change the key words.")
    elif (title_counter==1):
        print("\nFound {} title you might be interested in.\n".format(title_counter))
        print(LinksToSave)
    else:
        print("\nFound {} titles you might be interested in.\n".format(title_counter))
        print(LinksToSave)

if (__name__=="__main__"):
    crawl()
