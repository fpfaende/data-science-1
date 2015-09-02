# your road : 

# traffic for each day (regardless the hour)
# traffic for each hour (regardless the day)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

monday = 'green, green, orange, red, green, red, green'
tuesday = 'green, orange, orange, orange, green, red, green'

monday_values = monday.split(', ')
# +---------+---------+----------+
# | 'green' | 'green' | 'orange' |
# +---------+---------+----------+
# 0         1         2          3

monday_values[1]


traffic_values = {'green':1, 'orange':2, 'red':3, 'crimson':4}
print monday_values[0]
print traffic_values[ monday_values[0] ]

for color in monday_values:
	print color

for index in range(0,len(monday_values)
	):
	print monday_values[index]


days_of_the_week = {'monday':monday,'tuesday':tuesday}

for day in days_of_the_week:
	print day
	how_many_times_green = 0
	for value in days_of_the_week[day].split(', '):
		if value == 'green':
			how_many_times_green += 1
	print 'there is',how_many_times_green,'in',day