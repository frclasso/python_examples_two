#!/usr/bin/python

outFile = open("grades.txt", 'w')
print("Enter a grade (q to quit): ")
grade = raw_input()
while (grade != 'q'):
    outFile.write(grade + '\n')
    print("Enter a grade (q to quit): ")
    grade = raw_input()

outFile.close()
