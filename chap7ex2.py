#!/usr/bin/python

op1 = 0.0
op2 = 0.0
op = ''
while op1 != 'q':
    print('Enter first number ( q to quit): ')
    op1 = raw_input()
    if op1 == 'q':
        break;
   
    op1 = float(op1)
    print('Enter the second number ( q to quit): ')
    op2 = float(raw_input())
    print('Enter the operation (+,-,*,/): ')
    
    op = raw_input()
    if op == '+':
        print(op1 + op2)
    elif op == '-':
        print(op1 - op2)
    elif op == '*':
        print(op1 * op2)
    elif op == '/':
        print(op1 / op2)
    else:
        print('Did not recognize operator.')
   
