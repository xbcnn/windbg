#! python3
# coding: utf-8

import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool


def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        print 'COST: {}'.format(end - start)
    return wrapper

def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)

@profile
def nomultprocess():
    fib(35)
    fib(35)

@profile
def hasmultiprocess():
    pool = Pool(2)
    pool.map(fib, [35] * 2)

nomultprocess()
hasmultiprocess()