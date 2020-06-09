# Arxiv Harverster

This program is dedicated to automatically harvesting the Arxiv.org website for new and recent papers and filtering them out by the relevant key words.
## Arxiv-Harvester

Check out which website you would like to visit.
Then, save the response of your request in the file.
After opening the file, you can work with it locally after aving a response text if you wish.
It would be useful to use regular expressions, as the website response is
a text file.
A recent alternative is with BeautifulSoup package which can give pretty outputs from the HTML responses. This project has two analogous codes - one using only requests and regular expressions, and another using in addition Beaitiful Soup. Chose any and let's start harvesting!

Run as
|| python ArxivHarvester.py

If you are doing science and tired/lazy of manually going through arxiv every day, this program might be just right for you.

--------------------------

I wrote a recent edition / alternative approach to the same task using a BeatifulSoup. 
It works in the same way as the previous ArxivHarvester, just easier to find and retrieve a relevant information from a website.

Run as
|| python Beautiful_Soup_Harvester.py
