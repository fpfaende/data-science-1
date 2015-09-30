#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

db_conn = sqlite3.connect("/Users/fabien/workspace/complexcity/dianping/dianping/dianping.db")
db_cursor = db_conn.cursor()
query = '''
	select v.business_id, name, decoration_score, latitude, longitude
	from venues v 
	join venue_categories vc 
	on (v.business_id = vc.business_id)
	join categories c
	on (vc.category = c.category)
where 
	latitude > 31.3086 and 
	latitude < 31.315341 and 
	longitude > 121.3719 and 
	longitude < 121.3894 and
	decoration_score > 0 and 
	(c.parent = (select category from categories where en='food') or
	c.parent = (select category from categories where en='life'))
order by decoration_score desc;'''
results = db_cursor.execute(query).fetchall()

with open('best-design-in-west-gate.csv','w+') as f:
	f.write('id, name, design, latitude, longitude\n')
	for result in results:
		id = result[0]
		name = result[1]
		design = result[2]
		latitude = result[3]
		longitude = result[4]
		csvline = str(id) + ', '  + str(design) + ', ' + str(latitude) + ', ' + str(longitude) + ', ' +name.encode('utf-8') + '\n'
		f.write(csvline)


CARTODB.COM






