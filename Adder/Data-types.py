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
print()
# ***************************************
a = 8
b = 9
x = f'seven {a} {b}'

print('Starting in Python 3.6 the f-type is another way to format strings')
print("For instance x = f'seven {a} {b}'")
print('x is {}'.format(x))
print('_______________________________')
print()
