#!/usr/bin/python/

def flatten(x):
    for el in x:
        if type(el) == list:
            for y in flatten(el):
                yield y
        else:
            yield el

def main():
    x = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]
    print(list(flatten(x)))

if __name__ == "__main__":
    main()