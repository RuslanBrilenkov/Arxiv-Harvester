import urllib.request
#import urllib.parse

def Harvester():
    try:
        url = 'https://arxiv.org/list/astro-ph/new'
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        print(respData)
    except Exception as e:
        print(e)

if (__name__=="__main__"):
    Harvester()


