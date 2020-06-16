#!/bin/usr/python

from secrets import randbits
from random import randint

def generate_keys(bits):
    if_prime = False
    p = 0
    q = 0
    while not if_prime:
        p = randbits(bits)
        if_prime = muller_rabin(p)
    if_prime = False
    while not if_prime:
        q = randbits(bits)
        if_prime = muller_rabin(q)
    euler = (p-1)*(q-1)
    n = p*q

def euclid()

def muller_rabin(num):
    d = num - 1
    s = 0
    prime = True
    while d%2 == 0:
        s += 1
        d /= 2
    for _ in range(20):
        a = randint(2, num-2)
        x = (a**d)%num
        if x == 1 or x == num-1:
            continue
        j = 1
        while j < s and x != num-1:
            x = (x**2)%num
            if x == 1:
                prime = False
            j += 1
        if x != num - 1:
            prime = False
    return prime


def main():
    print()

if __name__ == "__main__":
    main()