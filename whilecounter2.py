#!/usr/bin/python

balance = 5000
rate = 1.02
year = 2001
while year <= 2017:
    balance  =  balance * rate
    print("Year: " + str(year) + " : " + "U$S " +  str(balance))
    year = year + 1
