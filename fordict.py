#!/usr/bin/python

numbers = {'Cinthia':'23456', 'Raymond':'345678', 'David':'65434321'}
print(numbers.keys())
print
print(numbers.values())
print
for key in numbers.keys():
    print(key + ' extension is ' + numbers[key])
