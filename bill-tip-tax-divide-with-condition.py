#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the initialization
bill = 103.5
tip = 'good'
state = 'CA'
persons = 3

# add the tip, default is 15%
if tip is 'bad':
	bill = bill + 0.10 * bill
elif tip is 'great':
	bill = bill + 0.20 * bill
else:
	bill = bill + 0.15 * bill

#add the tax, default is 6%
if state is 'CA':
	bill = bill + 0.0725 * bill
elif state is 'NY':
	bill = bill + 0.04 * bill
else:
	bill = bill + 0.06 * bill

#print thz result, rounded with two digit after decimal point
print 'Total bill is', round(bill,2),'$'
print 'Each person should pay', round(bill / persons, 2),'$'
