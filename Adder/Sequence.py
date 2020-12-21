#!/usr/bin/env python3

#This is referred to as a list, acts like array?
x = [ 1, 2, 3, 4, 5 ]

# lists are mutable
x[2] = 42

# tuples are like lists but are immutable - cannot be changed
# x = ( 1, 2, 3, 4, 5 )
print('Printing a list or tuple with 1, 2, 42, 4, 5')
for i in x :
    print(' is {}'.format(i))
print('__________________________')
print()
    
# an example of a all parameters in range
y = range(5)
print('use range with 1 parameter - (5)')
for i in y :
    print('i is {}'.format(i))
print('__________________________')
print()

# ****************************
w = range(5, 10)
print('use range with 2 parameters - (5, 10)')
for i in w :
    print('i is {}'.format(i))
print('__________________________')
print()

# ****************************
z = range(5, 10, 2)
print('use range with 3 parameters - (5, 10, 2)')
for i in z :
    print('i is {}'.format(i))
print('__________________________')
print()

# working with dictionaries
print('Now working with dictionaries...')
dictionary = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print("''one': 1, 'two': 2, etc'")
   
for i in dictionary:
    print('i is {}'.format(i)) 

print('This only prints the key though... what if we want value..')
print('__________________________')
print()

# *********************
print('Printing key and value of dictionary')
dictionary = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print("''one': 1, 'two': 2, etc'")
   
for k, v in dictionary.items():
    print('k is {}, v is {}'.format(k, v)) 

print('__________________________')
print()    