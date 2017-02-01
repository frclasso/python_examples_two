#!/usr/bin/python

def square(number):
    return number * number

print ("Enter a number: ")
num = int(input())
numsquared = square(num)
print(str(num) + " squared = " + str(numsquared))
