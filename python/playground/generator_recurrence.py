# !/usr/bin/env python3
class generator_fib(object):
    def __init__(self,max):
        for attr in self.fib(max):
            print(attr)
    def fib(self,max):
        n,a,b = 0,0,1
        while n < max:
            yield b
            a,b = b, a+b
            n += 1

class recurrence_fib(object):
    def __init__(self,max):
        for attr in range(max):
            print(self.fib(attr))
    def fib(self,max):
        if max == 0:
            return 1
        elif max == 1:
            return 1
        else:
            return self.fib(max - 2) + self.fib(max - 1)


example = generator_fib(10)
print('***************************')
example = recurrence_fib(10)



