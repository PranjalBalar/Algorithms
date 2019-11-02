# -*- coding: utf-8 -*-

#This program traverses through a graph using Breadth First Traversal
from collections import defaultdict
import Queue

class Node:
    def __init__(self, item, notVisited=True):
        self.item = item
        self.notVisited = notVisited


class Graph(object):
    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def getConnections(self, n):
        return self._graph.get(n)

q = Queue.Queue(maxsize=20)
g = Graph(directed=True)
node1 = Node("A", notVisited=True)
node2 = Node("B", notVisited=True)
node3 = Node("C", notVisited=True)
node4 = Node("D", notVisited=True)
node5 = Node("E", notVisited=True)
g.add(node1, node2)
g.add(node1, node4)
g.add(node2, node3)
g.add(node3, node5)
g.add(node3, node4)
g.add(node1, node5)

q.put(node1)
while not q.empty():
  a = q.get()
  if a.notVisited:
    x = g.getConnections(a)
    if x != None:
      for i in x:
        q.put(i) 
    print a.item
    a.notVisited = False
