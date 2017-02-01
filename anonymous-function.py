#!/usr/bin/python

#anonymous function
#lamda form

square = lambda x:  x*x
print(square(2))

numbers = [1,2,3,4]
numberssq = list(map(square, numbers))
print(numberssq)