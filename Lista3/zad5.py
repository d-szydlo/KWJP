#!/usr/bin/python/

def subsets(l):
    out = [[]]
    for el in l:
        out += list(map(lambda subset: subset + [el], out))
    return out


def main():
    l = [1, 2, 3]
    print(subsets(l))

if __name__ == "__main__":
    main()