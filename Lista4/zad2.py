#!/usr/bin/python

from random import randint, seed

def generate(height):
    seed()
    num = randint(0, 100)
    tree = [str(num), None, None]
    if height > 1:
        tree[1] = generate(height - 1)
        tree[2] = generate(height - 1)
    return tree

def bfs(tree):
    q = []
    q.append(tree)
    while len(q) != 0:
        yield q[0][0]
        if q[0][1] != None:
            q.append(q[0][1])
        if q[0][2] != None:
            q.append(q[0][2])
        q.pop(0)

def dfs(tree):
    s = []
    s.append(tree)
    while len(s) != 0:
        helper = s.pop(0)
        yield helper[0]
        if helper[2] != None:
            s.insert(0, helper[2])
        if helper[1] != None:
            s.insert(0, helper[1])
   

def main():
    tree =  ["1", ["2", ["4", ["8", None, None], ["9",None,None]], ["5",None,None]], ["3", ["6", None, None], ["7", None, None]]]
    print("Drzewo: {}".format(tree))
    print("BFS: {}".format(list(bfs(tree))))
    print("DFS: {}".format(list(dfs(tree))))

if __name__ == "__main__":
    main()
