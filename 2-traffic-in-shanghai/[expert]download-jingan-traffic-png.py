#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import shutil
import random
import time

payload = {}
payload['level']=19
payload['x']=105628
payload['y']=28440
payload['day']=3
payload['hour']=16
payload['t']=1441268387717
payload['v']='081'
payload['smallflow']=1

headers = {}
headers['Accept'] = 'image/webp,image/*,*/*;q=0.8'
headers['Accept-Encoding'] = 'gzip, deflate, sdch'
headers['Accept-Language'] = 'en,en-US;q=0.8,fr;q=0.6,fr-FR;q=0.4'
headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.78 Safari/537.36'

cookies = dict(gsScrollPos='0', BAIDUID='3D2D1E70490C57C093775D3BBEEFA511:FG=1', BIDUPSID='3D2D1E70490C57C093775D3BBEEFA511', PSTM='1435737859', H_PS_PSSID='16230_13551_1458_16571_14429_17012_12867_16938_14954_17000_16934_17004_17073_15504_12146_13932_16969_10634_16867_17050', MCITY='-%3A')

url = 'http://its.map.baidu.com:8002/traffic/HistoryService'
# http://its.map.baidu.com:8002/traffic/HistoryService?level=19&x=105628&y=28440&day=5&hour=16&t=1441440960128&label=web2D&v=081&smallflow=1

for day in range(0,7):
	for hour in range(0,24):
		payload['day']=day
		payload['hour']=hour
		r = requests.get(url, params=payload, headers=headers, cookies=cookies, stream=True)
		if r.status_code == 200:
			with open('data'+'-'+str(payload['day'])+'-'+str(payload['hour'])+'.png', 'wb') as fd:
				for chunk in r.iter_content(128):
					fd.write(chunk)

	sleeptime = random.uniform(0.5,1.0)
	time.sleep(sleeptime)