#!/usr/bin/python

try:
    print('Enter the name of file:   ')
    name = input()
    file = open(name, 'r')
except:
    print('Cannot open file')
    print('Enter the name of file to open: ')
    name = input()
    file = open(name, 'r')