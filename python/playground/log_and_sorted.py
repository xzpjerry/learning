# !/usr/bin/env python3

def mylog(func):
    def wrapper(*args, **keywords):
        print('Now excuating: %s' % func.__name__)
        tmp_func = func(*args, **keywords)
        print('END')
        return tmp_func
    return wrapper

@mylog
def by_name(data):
    return data[0]
@mylog
def by_socre(data):
    return data[1]





