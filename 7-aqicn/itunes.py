#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
from lxml import etree


r = requests.get("https://itunes.apple.com/cn/app/tips-4-candy-crush/id717348165?mt=8")
print r.status_code

data = r.text
tree = html.fromstring(r.text)

# result = etree.tostring(tree,pretty_print=True, method="html")
# print(result)

pm10div = tree.xpath('//div[@itemprop="price"]/text()')
print "candy crush price is",pm10div[0].strip().encode('utf-8')

