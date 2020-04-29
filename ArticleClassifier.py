
import requests
import pandas as pd
from bs4 import BeautifulSoup


def getAllDoxyDonkeyPosts(url, links):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    for a in soup.findAll('a'):
        try:
            url = a['href']
            title = a['title']
            if title == 'Older Posts':
                print(title, url)
                links.append(url)
                getAllDoxyDonkeyPosts(url, links)
        except:
            title = ""
    return


 def getDoxyDonkeyPost(TextUrl):
    response = requests.get(TextUrl)
    soup = BeautifulSoup(response.text)
    mydivs = soup.findAll("div", {'class':'post-body'})
    
    posts = []
    for div in mydivs:
        posts += map(lambda p : p.text.encode('ascii', errors = 'replace').replace(b"?", b" ").decode('ascii'), div.findAll('li'))
    return posts


if __name__ == '__main__':
	url = 'http://doxydonkey.blogspot.com/'
	links = []
	getAllDoxyDonkeyPosts(url, links)

	doxyDonkeyPosts = []
	for link in links:
	    doxyDonkeyPosts += getDoxyDonkeyPost(link)
	df = pd.DataFrame({'posts': doxyDonkeyPosts})
	df.to_csv('doxyDonkeyPosts.csv', index = False)
	df = pd.DataFrame({'links':links})
	df.to_csv('getDoxyDonkeyPostLinks', index = False)