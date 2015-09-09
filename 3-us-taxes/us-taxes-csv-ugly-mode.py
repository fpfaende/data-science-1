#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

tax = {}

with open('../csv/US-taxes.csv', 'rb') as csvfile:
	csvRows = csv.reader(csvfile, delimiter=',')
	next(csvRows)
	for csvRow in csvRows:
		name = csvRow[0]
		name = name.lower()
		if '(' in name:
			continue

		if '[' in name:
			name = name[:name.find('[')].strip()

		saleTax = csvRow[1].strip()
		foodTax = csvRow[2].strip()
		
		taxValue = 0
		if len(foodTax)>0 and '%' in foodTax:
			taxValue = float(foodTax[:foodTax.find('%')])/100
		else:
			taxValue = float(saleTax[:saleTax.find('%')])/100
		tax[name] = taxValue

print tax
