#!/usr/bin/python

answer = "Watson"
print("Here is a guessinf game. You get  three times.")
print("What is the name  of the computer that played on Jeopardy?")
response = raw_input()
if response == answer:
    print("That's right")
else:
    print("Sorry.Guess again!")
    response = raw_input()
    if response == answer:
        print("That's right")
    else:
        print("Sorry.Guess again.")
        response = raw_input()
        if response == answer:
            print("That's right")
        else:
            print("Sorry. No more guesses.The answer is " + answer + ".")
