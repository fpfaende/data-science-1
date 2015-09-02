#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the initialization
bill = 103.5
tip = 'good'
state = 'CA'
persons = 3
tips = {'good':0.15, 'bad':0.10, 'great':0.20}
taxes = {'CA':0.0725, 'FL':0.06, 'NY':0.04}

# the tips and the taxes
bill += bill * tips[ tip ]
bill += bill * taxes [state]
print 'Total bill is', round(bill,2) ,'$'
print 'Each person should pay', round(bill/persons, 2) ,'$'


