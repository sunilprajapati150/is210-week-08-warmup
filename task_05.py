#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Measuring my blood pressure"""

TEMP = raw_input('Enter your blood pressure: ')
TEMP = int(TEMP)

if TEMP <= 89:
    BP = 'Low'
elif 89 < TEMP <= 119:
    BP = 'Ideal'
elif 119 < TEMP <= 139:
    BP = 'Warning'
elif 139 < TEMP <= 159:
    BP = 'High'
else:
    BP = 'Emergency'

print 'Your Status is {}'.format(BP)
