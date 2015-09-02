#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Extracted from https://en.wikipedia.org/wiki/Sales_taxes_in_the_United_States
Transformed in openrefine
'''

import csv

def clean_name(name):
	if '[' in name:
		return name[:name.find('[')].strip()
	elif '(' in name:
		return None
	else:
		return name

def clean_tax(tax):
	return float(tax[:tax.find('%')])

taxes = {}
with open('csv/US-taxes.csv', 'rb') as csvfile:
	states = csv.reader(csvfile, delimiter=',')
	next(states)
	for state in states:
		name = state[0].strip()
		name = clean_name(name)
		
		base_tax = state[1].strip()
		food_tax = state[2].strip()
		
		if name is None:
			continue	
	
		if len(food_tax) > 0 and '%' in food_tax:
			tax = clean_tax(food_tax)
		else:
			tax = clean_tax(base_tax)

		taxes[name] = tax
print taxes


