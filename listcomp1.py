#!/usr/bin/python

grades = [71, 81, 77, 84]
print grades

#for i in range(len(grades)):
#    grades[i] = grades[i] + 5

grades = [grade + 5 for grade in grades]
print(grades)
