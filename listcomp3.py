#!/usr/bin/python

file = open('grades.txt')
grades = file.readlines()
print(grades)

# or
for i in range(len(grades)):
    grades[i] = grades[i].rstrip()
print(grades)

#or

grades = [grade.rstrip() for grade in open('grades.txt')]
print(grades)
