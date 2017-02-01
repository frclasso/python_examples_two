#!/usr/bin/python

grades = {'Cynthia': 88, 'David':77, 'Clayton':66}

it = iter(grades)
print(next(it))
print(next(it))
print(next(it))
for key in grades:
    print(key, grades[key])
