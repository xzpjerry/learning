#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''
import random
from myqueue import myqueue

def hotPotato(namelist):
    aqueue = myqueue()
    for name in namelist:
        aqueue.push(name)

    while aqueue.size() > 1:
        chosen_counting = random.randrange(0, aqueue.size())
        for i in range(chosen_counting):
            aqueue.push(aqueue.pop())
            print(aqueue)
        # Making a #times length cycle above
        print('Iteration ended ')
        aqueue.pop()
    
    return aqueue.pop()





print('\nLast one ->',hotPotato(["Bill","David","Susan","Jane","Kent","Brad"]))