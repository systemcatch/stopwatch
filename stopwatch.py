#!/usr/bin/env python3.4

from functools import wraps
import time

def stopwatch(func):
    @wraps(func)
    def wrapper(*args, **kw):
        t = time.time()
        res = func(*args, **kw)
        print(func.__name__, args, kw, time.time() - t)

        return res

    return wrapper


#debug

@stopwatch
def tester(n, r, **kwargs):
    sqr = [s**r for s in range(n)]
    return sum(sqr)


#tester(n=78976, r=2)
