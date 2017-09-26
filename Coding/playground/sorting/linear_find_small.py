#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import random

def test(datal):
    current_smallest = [datal[0]]
    for num in datal:
        if num > current_smallest[0]:
            current_smallest.pop()
            current_smallest.append(num)
    return current_smallest[0]

if __name__ == '__main__':

    datal = [random.randrange(i ** 2) for i in range(1000, 2000)]
    print(test(datal))



