#!/usr/bin/python/

import sys

def encode(input, output):
    array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    try:
        with open(input, "r") as in_file:
            conv = ""
            for line in in_file:
                for char in line:
                    helper = str(bin(ord(char)))
                    for i in range(0, 10-len(helper)):
                        conv += "0"
                    conv += helper[2:]
        flag = 0
        if len(conv)%6 == 2:
            conv += "0000"
            flag = 2
        elif len(conv)%6 == 4:
            conv += "00"
            flag = 4
        with open(output, "w") as out_file:
            i = 0
            while i < len(conv):
                index = int(conv[i:i+6],2)
                out_file.write(array[index])
                i += 6
            if flag == 2:
                out_file.write("=")
            elif flag == 4:
                out_file.write("==")
    except FileNotFoundError:
        print("Jestes pewien ze plik {} istnieje?".format(sys.argv[2]))
    except:
        print("Cos poszlo nie tak :c ")
        raise



def decode(input, output):
    array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    try:
        with open(input, "r") as in_file:
            conv = ""
            flag = 0
            for line in in_file:
                for char in line:
                    if char == "=":
                        flag += 1
                    else:
                        index = array.find(char)
                        index = str(bin(index))
                        for i in range(0, 8-len(index)):
                            conv += "0"
                        conv += index[2:]
            if flag == 1:
                conv = conv[:len(conv)-4]
            elif flag == 2:
                conv = conv[:len(conv)-2]
        with open(output, "w") as out_file:
            i = 0
            while i < len(conv):
                num = int(conv[i:i+8],2)
                out_file.write(chr(num))
                i += 8
    except IOError:
        print("Jestes pewien ze plik {} istnieje?".format(sys.argv[2]))
    except:
        print("Cos poszlo nie tak :c")
        raise

def initialize():
    if sys.argv[1] == "--encode":
        encode(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "--decode":
        decode(sys.argv[2], sys.argv[3])
    else:
        print("Nie ma takiej opcji jak {}".format(sys.argv[1]))

def main():
    if len(sys.argv) != 4:
        print("Podales nieprawidlowa liczbe argumentow")
        sys.exit(1)
    else:
        initialize()

if __name__ == "__main__":
    main()
