#!/usr/bin/env python3


def isVowel(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    else:
        return False


def numvowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if isVowel(string[i]):
            count += 1
    return count

print("Enter a string: ")
strng = input()
print("There are " + str(numvowels(strng)) + " vowels in the string.")
