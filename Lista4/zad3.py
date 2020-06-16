#!/usr/bin/python

from random import seed, randint

class Node(object):

    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, node):
        self.children.append(node)

    def display(self):
        print("Wartosc: {}\nDzieci:".format(self.value), end = " ")
        for child in self.children:
            print(child.value, end = " ")
        print()

def bfs(tree):
    q = []
    q.append(tree)
    while len(q) != 0:
        yield q[0].value
        for child in q[0].children:
            q.append(child)
        q.pop(0)

def dfs(tree):
    s = []
    s.append(tree)
    while len(s) != 0:
        helper = s.pop(0)
        yield helper.value
        for child in helper.children:
            s.insert(0, child)

def generate(height):
    seed()
    root = Node(randint(0,100))
    if height > 1:
        root.children.append(generate(height-1))
        root.children.append(generate(height-1))
    return root

def main():
    tree = generate(3)
    tree.display()
    for child in tree.children:
        child.display()
    print("BFS: {}".format(list(bfs(tree))))
    print("DFS: {}".format(list(dfs(tree))))

if __name__ == "__main__":
    main()
