#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

from myqueue import myqueue

def tester(aString):

    charQueue = myqueue()

    for ch in aString:
        charQueue.push(ch)

    while charQueue.size() > 1:
        rear = charQueue.pop()
        front = charQueue.pop(left=True)
        if rear != front:
            return False

    return True

print(tester('radar'))
print(tester('lsdkjfskf'))