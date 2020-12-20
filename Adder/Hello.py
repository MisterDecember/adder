#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

# variables
version = platform.python_version()
mod = 9
x = 24
y = 37
n = 0
a, b = 0, 1
fib_end = 10000
# primeno = 15

# arrays
words = ['adder', 'bear', 'chinchilla', 'dog', 'fox']

print('Hello, Mr. Azizi.')

# functions
def main() :
    message()

def message() :
    print('This is python version {}'.format(version))
    print('This is modification #{}'.format(mod))
    
def isprime(primeno) :
    if primeno <= 1 :
        return False
    for ex in range(2, primeno) :
        if primeno % ex == 0 :
            return False
        else :
            return True

def list_primes() :
    for primeno in range(1000) :
        if isprime(primeno) :
            print(primeno, end='  ', flush=True)
    print()
# examples of if statements

if __name__ == '__main__': 
    main()
    print() # line ending

print('Our currently set variables of x and y have been compared - ')    
if x > y :
    print('x > y:  x is {} and y is {}'.format(x,y))
elif x < y :
    print('x < y:  x is {} and y is {}'.format(x,y))
else :
    print("do something else")
    
print() # line ending

# examples of while loops
print('We have an array available with 5 (five) animals - allow me to demonstrate a While loop...')
while(n < 5):
    print(words[n])
    n += 1
    
print() # line ending
print('Here is the Fibonacci sequence (up to {}) , also using a While loop...'.format(fib_end))    
while b < fib_end :
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending
print() # line ending

# examples of for loops
print('It is recommended to use For loops where possible - it seems more efficient...')    
print('Here are the 5 (five) animals in our array - this time using a For loop...')
for i in words:
    print(i)

print() # line ending

# examples of functions

def function(n = 1):
    print(n)
print('this is a simple function')    
function()
print()

print('This is more advanced function... one that displays all prime numbers up to 1,000')
# if isprime(primeno) :
#     print(f'{primeno} is prime')
# else :
#     print(f'{primeno} is not prime')
list_primes()
