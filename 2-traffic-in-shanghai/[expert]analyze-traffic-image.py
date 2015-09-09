#!/usr/bin/python
# -*- coding: utf-8 -*-

import PIL
from PIL import Image
from matplotlib import pyplot as plt

import os
from os.path import join, getsize

greenDays = {'0':0,'1':0,'2':0,'3':0,'4':0, '5':0,'6':0}
orangeDays = {'0':0,'1':0,'2':0,'3':0,'4':0, '5':0,'6':0}
redDays = {'0':0,'1':0,'2':0,'3':0,'4':0, '5':0,'6':0}
crimsonDays = {'0':0,'1':0,'2':0,'3':0,'4':0, '5':0,'6':0}

greenHours = {}
orangeHours = {}
redHours = {}
crimsonHours = {}

orangeData = [[0 for i in range(0,24)] for j in range(0,7)]

for hour in range(0,24):
	greenHours[str(hour)]=0
	orangeHours[str(hour)]=0
	redHours[str(hour)]=0
	crimsonHours[str(hour)]=0

for root, dirs, files in os.walk('data'):
    for name in files:
		filename = name[:-4].split('-')
		day = filename[1]
		hour = filename[2]

		im = Image.open('data/'+name)  
		im = im.convert('RGB')
		w, h = im.size
		colors = im.getcolors(w*h)
		
		for count, color in colors:
			red = color[0]
			green = color[1]
			blue = color[2]

			if red in range(20,26) and green in range(188, 194) and blue in range(0, 6):
				greenHours[hour] += count
				greenDays[day] += count
			if red in range(250,256) and green in range(155, 161) and blue in range(22, 28):
				orangeHours[hour] += count
				orangeDays[day] += count
				orangeData[int(day)][int(hour)] = count
			if red in range(240,246) and green in range(47, 53) and blue in range(47, 53):
				redHours[hour] += count
				redDays[day] += count
			if red in range(185,191) and green in range(0, 6) and blue in range(0, 6):
				crimsonHours[hour] += count
				crimsonDays[day] += count

f,ax = plt.subplots()
ax.imshow(orangeData, interpolation='nearest')
# Move left and bottom spines outward by 10 points
ax.spines['left'].set_position(('outward', 10))
ax.spines['bottom'].set_position(('outward', 10))
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

f,(ax1, ax2)= plt.subplots(ncols=2)
x = range(0,7)
y1 = greenDays.values()
y2 = orangeDays.values()
y3 = redDays.values()
y4 = crimsonDays.values()
ax1.plot(x, y1,('#17BF00'),x, y2,('#FD9E30'), x, y3, ('#EF3237'),x, y4,('#BB0000'), linewidth=1.0)
ax1.set_xticklabels( ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

x = range(0,24)
y1 = greenHours.values()
y2 = orangeHours.values()
y3 = redHours.values()
y4 = crimsonHours.values()
ax2.plot(x, y1,('#17BF00'),x, y2,('#FD9E30'), x, y3, ('#EF3237'),x, y4,('#BB0000'), linewidth=1.0)


plt.show()
