#!/usr/bin/env python
# -*- coding: utf-8 -*-

monday_data = 'green, green, green, green, green, green, orange, red, orange, red,green, red, orange,green,green, green, green, green, green, green, orange, red, orange, red'
tuesday_data = 'green, orange, orange, orange, green, red, green'

days_of_the_week = {'monday':monday_data,'tuesday':tuesday_data}

for day in days_of_the_week:
	hmtg = 0
	hmto = 0
	hmtr = 0
	
	for value in days_of_the_week[day].split(', '): #here is a comment
		if value == 'green':
			hmtg += 1		
		elif value =='orange':
			hmto += 1
		else:
			hmtr += 1

	how_bad_is_the_traffic = hmtg + hmto * 2 + hmtr *3
	# print 'there is',hmtg,'green in',day
	# print 'there is',hmto,'orange in',day
	# print 'there is',hmtr,'red in',day
	print day[0:2],''.join('*' for i in range(0,how_bad_is_the_traffic))












