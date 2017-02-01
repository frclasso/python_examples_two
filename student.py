#!/usr/bin/python

class Student:
    #fields => name, id , grades(list)
    grades = []

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def addGrade(self, grade):
        self.grades.append(grade)

    def showGrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

stu1 = Student('Jones', '123456')
stu1.addGrade(88)
stu1.addGrade(80)
stu1.addGrade(86)
stu1.addGrade(81)
print(stu1.showGrades())