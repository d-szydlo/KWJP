#!/usr/bin/python/

import sys

def main():
    try:
        filename = str(sys.argv[1])
    except IndexError:
        print("Halo, nie dales pliku")
        sys.exit(1)

    byte_counter = 0
    word_counter = 0
    line_counter = 0
    max_length = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                line_counter += 1
                byte_counter += len(line)
                if len(line) > max_length:
                    max_length = len(line) #liczone z bialym znakiem na koncu linii
                word_counter += len(line.split())
        print("liczba bajtow: {}\nliczba slow: {}\nliczba linii: {}\nmaksymalna dlugosc linii: {}".format(
                byte_counter, word_counter, line_counter, max_length))
    except:
        print("Cos poszlo nie tak :c")
    return

if __name__ == "__main__":
    main()