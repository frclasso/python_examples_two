#!/usr/bin/python

import newton


def square(number):
    print("Not from the newton module")
    return number * number

num = 12
print("Square form newton.py")
print(newton.square(num))

print("")
print("Square from main program")
print(square(num))