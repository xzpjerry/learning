# !/usr/bin/env python3


class Fib(object):
    """docstring for Fib"""

    def __init__(self, max=1000):
        self.f0, self.f1 = 0, 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.f0, self.f1 = self.f1, self.f0 + self.f1
        if self.f0 > self.max:
            raise StopIteration()
        return self.f0

    def __getitem__(self, index):
        self.f0 = 1
        for i in range(index):
            self.f0, self.f1 = self.f1, self.f0 + self.f1
        return self.f0


for num in Fib(10):
    print(num)

print('**********')

for i in range(10):
    print(Fib()[i])
