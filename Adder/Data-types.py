#!/usr/bin/env python3

x = 'seven' 
print('This is an example of using the type function to determine the data-type')
print('x is {}'.format(x))
print(type(x))
print('_______________________________')
print()

# ***************************************
x = 'seven {} {}'.format(8, 9)
print('This is an example of using the format function to insert value in output')
print('x is {}'.format(x))
print('_______________________________')
print()

# ***************************************
x = 'seven {1} {0}'.format(8, 9)
print('This is an example of using the format function to insert value in output, but controlling the order in which they appear')
print('x is {}'.format(x))
print('_______________________________')
