#!/usr/bin/python

try:
    print('Enter a numerator: ')
    numer = int(input())
    print('Enter a denominator: ')
    denom = int(input())
    quotient = numer / denom
    print(quotient)
except:
    print("Cannot divide by zero.")
    print("Enter a new denominator: ")
    denom = int(input())
    quotient = numer / denom
    print(quotient)