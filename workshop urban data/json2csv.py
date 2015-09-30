#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json

with open('shanghai-flikr.json','r') as jsonfile:
	data = json.load(jsonfile)
print data
with open ('shanghai-flickr.csv','w+') as csvfile:
	line = 'id, title, longitude, latitude'+'\n'
	csvfile.write(line)
	for photo in data['photos']['photo']:
		line = photo['id'] + ',' + ',' + str(photo['longitude']) + ',' + str(photo['latitude'])+'\n'
		csvfile.write(line)
