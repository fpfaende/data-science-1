#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json

data = []

with open('../csv/HSK_Level_1_(New_HSK).csv') as csvfile:
	vocabularyList = csv.reader(csvfile)
	next(vocabularyList)
	for line in vocabularyList:
		order = line[0]
		hskOrder = line[1]
		chinese = line[2]
		pinyin = line[3]
		english = line[4]

		data.append({'cn':chinese, 'en':english,'pinyin':pinyin})

print data


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)