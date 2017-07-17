#!/usr/bin/env python3.4

from functools import wraps
import time

def stopwatch(func):
    """Decorator used for timing functions."""
    
    @wraps(func)
    def wrapper(*args, **kw):
        t = time.time()
        res = func(*args, **kw)
        print(func.__name__, args, kw, time.time() - t)

        return res

    return wrapper

