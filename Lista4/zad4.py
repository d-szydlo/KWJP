#!/usr/bin/python

from inspect import getfullargspec

class Overloading(object):

    def __init__(self):
        self.funcs = {}

    def __call__(self, *args):
        func = self.funcs.get(str(len(args)))
        return func(*args)

    def add_func(self, args_num, func):
        self.funcs[str(args_num)] = func

over = Overloading()

def overload():
    def modified(func):
        global over
        args = getfullargspec(func).args
        over.add_func(len(args), func)
        return over
    return modified

@overload()
def norm(x, y):
    return (x**2 + y**2)**0.5     

@overload()
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)

def main():
    print(f"norm(2,4) = {norm(2,4)}")
    print(f"norm(2,3,4) = {norm(2,3,4)}")
    

if __name__ == "__main__":
    main()
