import sqlite3
import requests

db_conn = sqlite3.connect("/Users/fabien/workspace/data-science-1/6-unsplash/unsplash.sqlite")
db_cursor = db_conn.cursor()

done = False
urlFromThePast = ''
while not done:
	url = db_cursor.execute("select url from urls where downloaded = 0").fetchone()
	if urlFromThePast == url[0]:
		query = "update urls set downloaded = 2 where url = '"+url[0]+"'"
		db_cursor.execute(query)
		db_conn.commit()
		continue

	print "downloading",url[0]
	r = requests.get(url[0], stream=True, )
	
	path = r.url
	path = path.split('/')[-1]
	path = path[:path.find('?')]

	if '.jpg' not in path.lower():
		path = path+'.jpg'
	if r.status_code == 404:
		query = "update urls set downloaded = 2 where url = '"+url[0]+"'"
		db_cursor.execute(query)
		db_conn.commit()
		continue
	if r.status_code == 200 or r.status_code == 302:
		with open('pictures/'+path, 'wb') as f:
			for chunk in r:
				f.write(chunk)
		query = "update urls set downloaded = 1 where url = '"+url[0]+"'"
		db_cursor.execute(query)
		db_conn.commit()
		print 'done',url[0], path
	urlFromThePast = url[0]