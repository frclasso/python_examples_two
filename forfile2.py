#!/usr/bin/python
from __future__ import print_function	
sum = 0
count = 0
for grade in open('grades.txt'):
    print(grade, end='')
    sum = sum + int(grade)
    count = count + 1
average = sum / count
print('Average: ' + str(average))
