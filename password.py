#!/usr/bin/python3
# -*- coding:utf-8 -*-


def checkio(data):
    upperConut = 0
    lowCount = 0
    numCount = 0
    if len(data) < 10:
        return False
    for a in data:
        if a.isupper():
            upperConut = upperConut + 1
        elif a.islower():
            lowCount = lowCount + 1
        elif a.isdigit():
            numCount = numCount + 1
    if upperConut > 0 and lowCount > 0 and numCount > 0:
        return True
    else:
        return False



# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")