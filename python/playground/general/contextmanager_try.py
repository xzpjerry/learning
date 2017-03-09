#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

from contextlib import contextmanager

class Printer(object):

    def __init__(self, name):
        self.name = name
        print(self.name)

@contextmanager
def do_sth_before_and_after_printer():
    print('I can do sth before the others!')
    yield
    print('I have already done sth after others!')

with do_sth_before_and_after_printer() as sth:
    tmp = Printer('Tom')
    '''
    ➜  playground git:(master) ✗ python3 contextmanager_try.py
    I can do sth before the others!
    Tom
    I have already done sth after others!
    '''
