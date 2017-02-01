#!/usr/bin/python
import functools


def square(number):
    return number * number


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def sum(x,y):
    return x + y

print("Square function")
numbers = [1,2,3,4]
print(numbers)
numberssq = list(map(square, numbers))

print("")
print("Even function")
numbers = list(range(1,11))
print(numbers)
evens = list(filter(even, numbers))
print(evens)
print("")

print("Sum Function")
numbers = list(range(1, 11))
print(numbers)
sum = functools.reduce(sum, numbers)
print("The sum is of the range is: " + str(sum))

