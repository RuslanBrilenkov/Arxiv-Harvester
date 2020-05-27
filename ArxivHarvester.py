import urllib.request
#import urllib.parse

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

def OpenResponse():
	'''
	Reading saved (.txt) data of website response
	'''
	with open("Arxiv_data.txt", "r") as file:
		Data = file.read()
	print(Data)

if (__name__=="__main__"):
	#Harvester()
	OpenResponse()


