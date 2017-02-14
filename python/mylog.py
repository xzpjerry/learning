#!/usr/bin/env python3

logging_counter = 0


def mylog(level='Normal'):
    def decorater(func):
        from functools import wraps
        import inspect

        @wraps(func)
        def wrapper(*args, **kw):
            if level == 'Normal':
                global logging_counter
                logging_counter += 1
                print('It\'s %d time(s) excuteing --\'%s\'-- func, start!' %
                      (logging_counter, func.__name__))
                args_name = inspect.getargspec(func)[0]
                args_dict = dict(zip(args_name, args))
                print(args_dict)
                return func(*args, **kw), print('%d time(s) excuteing ended.' % logging_counter)
            else:
                return func(*args, **kw), print('Something Wrong!!')
        return wrapper
    return decorater
