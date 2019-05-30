# -*- coding: utf-8 -*-

#This program uses double hashing to create a hash table with less clusters 
l = [None] * 10

class HashTable():

	def __init__(self, lst):
		self.lst = lst
		self.len = len(self.lst)

	def add(self, x):
		n1 = hash(x) % self.len
		if self.lst[n1] == None:
			self.lst[n1] = x
			return self.lst
		else:
			n2 = (hash(x) % 7) + 3
			l = []
			pos = self.check_add(n1, n2, 1, l)
			if (pos != None) :
				self.lst[pos] = x
				return self.lst
			else :
				return None

	def check_add(self, n1, n2, m, l):
		pos = (n1 + (m * n2)) % self.len
		if (pos in l) :
			return None
		elif (self.lst[pos] == None) :
			return pos
		else :
			l.append(pos)
			return self.check_add(n1, n2, m + 1, l) 

	def get(self, x):
		n1 = hash(x) % self.len
		if self.lst[n1] == x:
			return n1
		else:
			n2 = (hash(x) % 7) + 3
			l = []
			pos = self.check_get(x, n1, n2, 1, l)
			if (pos != None) :
				return pos
			else :
				return None

	def check_get(self, x, n1, n2, m, l):
		pos = (n1 + (m * n2)) % self.len
		if (pos in l) :
			return None
		elif (self.lst[pos] == x) :
			return pos
		else :
			l.append(pos)
			return self.check_add(n1, n2, m + 1, l) 

h = HashTable(l)