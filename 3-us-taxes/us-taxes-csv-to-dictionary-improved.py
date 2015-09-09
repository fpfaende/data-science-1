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

def find_state_from_abbrev(abbrev, states):
	for (key, value) in states.items():
		if value['short'] == abbrev:
			return key

states = {}
with open('../csv/US-states.csv', 'rb') as csvfile:
	statesNames = csv.reader(csvfile, delimiter=',')
	next(statesNames)
	for stateNames in statesNames:
		name = stateNames[0].strip()
		name = clean_name(name)
		states[name] = {'short':stateNames[1]}

with open('../csv/US-taxes.csv', 'rb') as csvfile:
	statesTaxes = csv.reader(csvfile, delimiter=',')
	next(statesTaxes)
	for stateTaxes in statesTaxes:
		name = stateTaxes[0].strip()
		name = clean_name(name)

		base_tax = stateTaxes[1].strip()
		food_tax = stateTaxes[2].strip()
		
		if name is None:
			continue	

		if len(food_tax) > 0 and '%' in food_tax:
			tax = clean_tax(food_tax)
		else:
			tax = clean_tax(base_tax)

		states[name]['tax'] = tax/100

print states

print 'tax for Arkansas is', states['Arkansas']['tax']
print 'tax for MD is', states[find_state_from_abbrev('MD',states)]['tax']
