# -*- coding: utf-8 -*-

#This program finds the shortest path between two nodes in a graph
def AllPairsShortestPath(g):
	dist = map(lambda i : map(lambda j : j , i) , g)

	for k in range(4):
		for a in range(4):
			for b in range(4):
				new_dist = dist[a][k] + dist[k][b]
				if new_dist < dist[a][b]:
					dist[a][b] = new_dist

	printSol(dist)


def printSol(dist): 
    for i in range(4): 
        for j in range(4): 
            if(dist[i][j] >= 100000): 
                print "%7s" %("None"), 
            else: 
                print "%7d\t" %(dist[i][j]), 
            if j == 4-1: 
                print "" 

graph = [[0,10,4,1000000], 
         [100000,0,1000000,4], 
         [100000, 4, 0, 10], 
         [100000, 100000, 1000000, 0]] 

AllPairsShortestPath(graph)