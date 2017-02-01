#!/usr/bin/python

#tax table
# U$0 - U$240 = 0%
# U$241  - U$480 = 15%
# U$481 - U$28%


def tax(amount):
    if amount < 240:
        return 0
    elif amount > 240 and amount <= 480:
        return amount * .15
    else:
        return amount * .28


def netpay(grosspay):
    return grosspay - tax(grosspay)


print('Enter the amount: ')
amount = int(input())
print("The tax is  U$" + str(tax(amount)))

print("Enter gross pay")
gp = int(input())
print("Net pay is U$" + str(netpay(gp)))