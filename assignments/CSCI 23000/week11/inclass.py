"""
Name: Cayden Young
Course: CSCI 23000
Assignment: In class assignment
Date: 11/09/2023
"""


def addDigitsRec(aString, n):
    if n == 0:
        return int(aString[0])
    else:
        return int(aString[n]) + addDigitsRec(aString, n - 1)


def checkIfOnlyDigits(aString):
    return aString.isdigit()


aIntString = "112"
if checkIfOnlyDigits(aIntString):
    print(addDigitsRec(aIntString, len(aIntString) - 1))
else:
    print("Cannot add up digits")
