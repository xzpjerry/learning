# !/usr/bin/env python3

class animal(object):
    def __init__(self):
        self.run()
    def run(self):
        print('This is an animal and it\'s runing')

class flyMixIn(object):
    def __init__(self):
        print('I\'ll be overrided' )
    def fly(self):
        print('I can fly by the way.')

'''
When existing multiple
the same name parant func,
the mose outside one would
be overrided
'''

class cat(animal, flyMixIn):
    def __init__(self):
        super().__init__()
        self.fly()

class dog(animal):
    pass