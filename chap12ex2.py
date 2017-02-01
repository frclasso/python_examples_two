#!/usr/bin/python

#in y humble opinion
#IMHO


def first(word):
    return word[0]

def acronym(words):
    acro = ''
    acro = acro.join(list(map(first, words))).upper()
    return acro

print("Method one")
words = ['in', 'my', 'humble', 'opinion']
acro = list(map(first, words))
print(acro)
print("")

print("Method two")
#acro = ''
#acro = acro.join(list(map(first, words))).upper()
acro = acronym(words)
print(acro)