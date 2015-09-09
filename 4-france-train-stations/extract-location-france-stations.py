#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

cleanedData = []
with open('../csv/data-gouv-gare-SNCF.csv', 'rU') as csvfile:
	gares = csv.reader(csvfile, delimiter=';')
	next(gares)
	for gare in gares:
		name = gare[1]
		latitude = float(gare[3].replace(',', '.'))
		longitude = float(gare[4].replace(',', '.'))
		
		cleanedData.append([name, latitude, longitude])

with open('./localized-stations.csv', 'wb') as csvfile:
    stationWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    stationWriter.writerow(['name', 'latitude', 'longitude'])
    for data in cleanedData:
    	stationWriter.writerow(data)
