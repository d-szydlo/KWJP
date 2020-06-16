#!/usr/bin/python/

import os
import sys

def to_lower(path):
    os.chdir(path)
    dirs = os.listdir(path)
    for dir in dirs:
        if os.path.isdir(path + "/" + dir):
            to_lower(path + "/" + dir)
            os.rename(path + "/" + dir, path + "/" + dir.lower())


def main():
    try:
        path = str(sys.argv[1])
        if path.startswith("./"):
            path = os.getcwd() + path[2:]
        to_lower(path)
    except IndexError:
        print("Halo, nie dales katalogu")
        sys.exit(1)
    except FileNotFoundError:
        print("Nie ma takiego katalogu jak {}".format(sys.argv[1]))
        sys.exit(1)
    return

if __name__ == "__main__":
    main()