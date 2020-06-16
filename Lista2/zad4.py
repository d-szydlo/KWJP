#!/usr/bin/python

import os
import sys
import hashlib

paths = []
hashes = []
sizes = []

def get_data(path):
    os.chdir(path)
    for root, dirs, files in os.walk(path, topdown=True):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
            size = os.path.getsize(filepath)
            sizes.append(size)
            with open(filepath, "r") as f:
                content = f.read()
                content = hashlib.md5(content.encode()).hexdigest()
                hashes.append(content)

def check_reps(path):
    os.chdir(path)
    get_data(path)
    index = 0
    while index < len(paths):
        c_size = sizes[index]
        c_hash = hashes[index]
        c_path = paths[index]
        matches = []
        i = 0
        while i < len(paths):
            if sizes[i] == c_size and hashes[i] == c_hash and c_path != paths[i]:
                matches.append(paths[i])
                paths.pop(i)
                sizes.pop(i)
                hashes.pop(i)
                i -= 1
            i += 1
        if len(matches) > 0:
            print("-"*30)
            matches.insert(0, c_path)
            for name in matches:
                print(name)
        index += 1


def main():
    try:
        os.path.isdir(sys.argv[1])
    except IndexError:
        print("Nie podano argumentow")
    except FileNotFoundError:
        print("Katalog {} nie istnieje :c".format(sys.argv[1]))

    if os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        if path.startswith("./"):
            path = os.path.join(os.getcwd(), path[2:])
        check_reps(path)
    else:
        print("{} nie jest katalogiem :c".format(sys.argv[1]))

if __name__ == "__main__":
    main() 