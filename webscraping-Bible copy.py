import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#BUILD URL

webpage = 'https://biblehub.com/asv/john/'

chapter = random.randint(1,21)

url = webpage + str(chapter) + '.htm'

print(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

#PARSE

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

#SCRAPE WEBPAGE

verses = soup.findAll('div',attrs={'class':'chap'})

for verse in verses:
    verse_list = verse.text.split('.')

#print(verse_list)

myverse = random.choice(verse_list)

print(f"Chapter: {chapter}, Verse:{myverse}")



