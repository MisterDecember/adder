#!/usr/bin/env python3

x = .1 + .1 + .1 - .3
print('This is how .1 + .1 + .1 - .3 adds up to:')
print('x is {}'.format(x))
print(type(x))
print('We must account for the precision Python attempts by using the import function to use something like decimal')
print("_____________________________")
print()
# *********************************
from decimal import *

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
print('This is the output using the Decimal function')
print("_____________________________")
