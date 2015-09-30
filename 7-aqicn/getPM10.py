#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from lxml import etree


r = requests.get("http://www.stateair.net/web/post/1/4.html")
print r.status_code

data = r.text
tree = html.fromstring(r.text)

# result = etree.tostring(tree,pretty_print=True, method="html")
# print(result)

pm10div = tree.xpath('//td[@class="aqi_3"]/text()')
print "pollution in shanghai now is",pm10div[0].strip()

