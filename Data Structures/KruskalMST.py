#-*- coding: utf-8 -*-

#This program creates a minimum spanning tree using Kruskal's algorithm
#The complexity of this program is O(E*log(V)) where E is the number of edges and V is the number of vertices in the graph 
from collections import defaultdict

class KruskalMST:

	def __init__(self, v):
		self.v = v
		self.g =[]

	def add_edge(self, a, b, c):
		self.g.append([a, b, c])
		return True

	def parent(self, p, x):
		if p[x] == x:
			return x
		return self.parent(p, p[x])

	def unionFind(self, p, r, x, y):
		a = self.parent(p, x)
		b = self.parent(p, y)
		if r[a]<r[b]:
			p[a] = b
		elif r[a] > r[b]:
			p[b] = a
		else:
			p[y] = x
			r[x] += 1

	def MST(self):
		self.g = sorted(self.g, key = lambda item:item[2])
		result =[]
		par =[]
		rank =[0] * self.v
		e = 0
		r = 0

		for i in range(self.v):
			par.append(i)
			rank.append(0)
		while r < (self.v - 1):
			a, b, c = self.g[e]
			e += 1
			x = self.parent(par, a)
			y = self.parent(par, b)
			if x != y:
				r += 1
				result.append([a, b, c])
				self.unionFind(par, rank, x, y)

		for a, b, c in result:
			print ("%d ---> %d = %d" % (a, b, c))
		

g = KruskalMST(9)
g.add_edge(0, 1, 12)
g.add_edge(0, 7, 23)
g.add_edge(1, 2, 23)
g.add_edge(1, 7, 37)
g.add_edge(2, 3, 21)
g.add_edge(2, 5, 12)
g.add_edge(3, 4, 27)
g.add_edge(3, 5, 45)
g.add_edge(5, 4, 30)
g.add_edge(6, 5, 6)
g.add_edge(7, 6, 4)
g.add_edge(7, 8, 21)
g.add_edge(8, 2, 7)
g.add_edge(8, 6, 18)
g.MST()
