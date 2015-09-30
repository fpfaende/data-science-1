#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22shanghai%22)%20%20%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
print r.status_code

data = r.json()
temp = data['query']['results']['channel']['item']['condition']['temp']
text = data['query']['results']['channel']['item']['condition']['text']
city = data['query']['results']['channel']['location']['city']

print 'hello, it is', text, 'with a temperature of', temp, '°C in', city