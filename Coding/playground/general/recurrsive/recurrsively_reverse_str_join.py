#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import re
def reverseStr(astr):
    if len(astr) == 1:
        return astr
    else:
        return astr[1:] + astr[0]

def isPalindrome(astr):
    astr = ''.join(re.split(r'[\s\'\;\.\-]', astr)).upper()
    print(astr)
    if len(astr) <= 1:
        return True
    if astr[0] == astr[-1]:
        return isPalindrome(astr[1:-1])
    return False

print(isPalindrome('Go hang a salami; I\'m a lasagna hog.'))
print(isPalindrome('Wassamassaw'))