#!/usr/bin/python

from newton import average, square

num1 = 199
num2 = 78

avg = average(num1, num2)
print("The average is: " + str(avg))
print("The square of the average " + str(square(avg)))