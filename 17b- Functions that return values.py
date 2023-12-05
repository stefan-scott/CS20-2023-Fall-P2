# Functions that return Values (fruitful functions)
# Mr. Scott
# Dec 4, 2023

import math

# built-in functions with return values
print(abs(4))  #  |-5| → 5
print(abs(-4))

print(math.pow(2,3)) #2^3  (2x2x2)
print(math.pow(7,2)) #7^2  (7x7)

print(max(1,2,3,4))  #max returns the largest value
print(max(50, 99, 88)) #there is also a min function

def custom_square(orig_number):
    #take orig_number and compute its square (^2)
    result = orig_number * orig_number
    return result  #BETTER DESIGN
                   #allows the program to decide how to use the output
    
#We use return values in primarily 3 ways
#1: store in a variable
my_square = custom_square(11)

#2: print it out
print(custom_square(7))

#3: use return value as INPUT for another method (non-print)
print(max(99, 88, custom_square(10)))
    
    
    