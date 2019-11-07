# -*- coding: utf-8 -*-

#This program creates a minimum spanning tree using prim's algorithm
#The complexity of this program is O((V+E)*log(V)) where V is the number of vertices and E is the number of edges in the graph 
import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printMST(self, parent): 
        print "Edge \tWeight"
        x = 0
        for i in range(1, self.V): 
            x += self.graph[i][ parent[i] ]
            print parent[i], "-", i, "\t", self.graph[i][ parent[i] ] 

        print "Total Weight:", "\t", x
  
    def minKey(self, key, mstSet): 
        min = sys.maxint 
  
        for i in range(self.V): 
            if key[i] < min and mstSet[i] == False: 
                min = key[i] 
                min_index = i 
  
        return min_index 
  
    def primMST(self): 
  
        key = [sys.maxint] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 
        parent[0] = -1  
  
        for cout in range(self.V): 
  
            x = self.minKey(key, mstSet) 
            mstSet[x] = True
  
            for i in range(self.V): 
                if self.graph[x][i] > 0 and mstSet[i] == False and key[i] > self.graph[x][i]: 
                        key[i] = self.graph[x][i] 
                        parent[i] = x 
  
        self.printMST(parent) 
  
g = Graph(5) 
g.graph = [ [0, 10, 20, 0, 0], 
            [10, 0, 30, 5, 0], 
            [20, 30, 0, 15, 6], 
            [0, 5, 15, 0, 8], 
            [0, 0, 6, 8, 0]] 
  
g.primMST(); 