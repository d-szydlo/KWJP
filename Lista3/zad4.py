#!/usr/bin/python/

def quick_sort(l):
    if len(l) > 1:
        left = quick_sort(list(filter(lambda num: num < l[0], l)))
        right = quick_sort(list(filter(lambda num: num > l[0], l)))
        left.append(l[0])
        left += right
        return left
    else:
        return l


def main():
    l = [2, -47, 1, 1, 45, 100, -345]
    print(quick_sort(l))

if __name__ == "__main__":
    main()