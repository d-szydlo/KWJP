#!/usr/bin/python/

from functools import reduce

def sum_file(filename):
    with open(filename, "r") as f:
        num = list(int(line.split()[-1]) for line in f)
        num = reduce(lambda x, y: x + y, num)
        return num


def main():
    print(sum_file("test.txt"))

if __name__ == "__main__":
    main()