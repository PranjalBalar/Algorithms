# -*- coding: utf-8 -*-

#This program finds whether or not there is a cycle in a graph
from collections import defaultdict 

class Graph:
    def __init__(self, v):
        self.v = v
        self.g = defaultdict(list)

    def add(self, x, y):
        self.g[x].append(y)

    def parent(self, p, x):
        if p[x] == -1:
            return x
        elif p[x] != -1:
            return self.parent(p, p[x])

    def unionFind(self, p, x, y):
        a = self.parent(p, x)
        b = self.parent(p, y)

        p[a] = b

    def find(self):
        p = [-1] * self.v

        for i in self.g:
            for j in self.g[i]:
                x = self.parent(p, i)
                y = self.parent(p, j)

                if x == y:
                    print "There is a Cycle"
                    return -1
                self.unionFind(p, x, y)

g = Graph(3)
g.add(0, 1)
g.add(1, 2)
g.add(2, 0)

g.find()