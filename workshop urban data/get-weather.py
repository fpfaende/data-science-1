#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

# r = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%202151849%20and%20u%3D%20'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")

r = requests.get("http://www.complexcity.org")

print r.text.encode('utf-8')
# data =  json.loads(r.text)

# condition = data['query']['results']['channel']['item']['condition']['text']
# temperature = data['query']['results']['channel']['item']['condition']['temp']

# print 'Hello Shanghai, it is', condition, 'with', temperature + 'c today'