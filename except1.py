#!/usr/bin/python

def calc(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2

cont = 'y'
while cont != 'n':
    print('Enter the first number: ')
    num1 = int(input())
    print('Enter the second number: ')
    num2 = int(input())
    print('Enter the operation: ')
    op = input()
    if op == '/' and num2 == 0:
        print('Cannot dived by zero')
        continue
    else:
        print(calc(num1, num2, op))
    print("Dou you want to continue? (y/n")
    cont = input()