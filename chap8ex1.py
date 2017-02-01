#!/usr/bin/python

print 'Enter a number: '
num = int(input())
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(str(num) + '! = ' + str(fact))
