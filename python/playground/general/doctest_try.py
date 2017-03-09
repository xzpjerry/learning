
def fact(n):
    '''
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(6)
    720
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 0:
        raise ValueError()
    elif n <= 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('All test passed')