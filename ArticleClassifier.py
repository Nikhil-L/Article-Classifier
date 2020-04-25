
import requests
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


if __name__ == '__main__':
	url = 'http://doxydonkey.blogspot.com/'
	links = []
	getAllDoxyDonkeyPosts(url, links)