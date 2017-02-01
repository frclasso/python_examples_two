#!/usr/bin/python

#numbers = range(1, 11)
#it = iter(numbers)
#print(next(it))

import os
files = os.popen('ls *.py')
fileit = iter(files)
for file in files:
    print(files)
