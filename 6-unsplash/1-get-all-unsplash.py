import requests
from BeautifulSoup import BeautifulSoup

import random
import time

urls = []
for i in range(1,264):
	url = 'https://unsplash.com/new?page=' + str(i)
	r = requests.get(url)
	rawHTML = r.text
	soup = BeautifulSoup(rawHTML)
	for tag in soup.findAll('a', href=True):
		if 'photos' in tag['href']:
			urls.append('https://unsplash.com'+tag['href'])
	print 'page ',i,'done'
	sleeptime = random.uniform(0.5,1.0)
	time.sleep(sleeptime)

with open('urls.csv', 'w') as f:
	for url in urls:
		f.write(url+'\n')
