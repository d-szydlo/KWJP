#!/usr/bin/python
from time import time, sleep

def func_time(func):
    def inner(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        print(time()-start)
        return ret
    return inner

@func_time
def wait_func(t):
    sleep(t)
    return t

def main():
    wait_func(3)

if __name__ == "__main__":
    main()

