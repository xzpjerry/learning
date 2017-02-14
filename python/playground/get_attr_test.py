#!/usr/bin/env python3


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print('getattr process')
        print('path is now:', self._path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, user = ''):
        print('call process')
        print('path is now:', self._path)
        return self.__getattr__(':' + user)

    __repr__ = __str__

example = Chain().something('sth').repos('another things')
print(example)
# '/something/:sth/repos/:another things'
