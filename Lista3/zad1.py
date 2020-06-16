#!/usr/bin/python/

def transpose(matrix):
    res = [row.split() for row in matrix]
    res = [[res[i][j] for i in range(len(res))] for j in range(len(res))]
    res = [" ".join(row) for row in res] 
    return res

def main():
    matrix = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
    print(transpose(matrix))

if __name__ == "__main__":
    main()