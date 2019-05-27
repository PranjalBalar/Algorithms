# -*- coding: utf-8 -*-

#This program creates a hash table using linear probing 
l = [None] * 10

class HashTable():

	def __init__(self, lst):
		self.lst = lst
		self.len = len(self.lst)

	def add(self, x):
		n = hash(x) % self.len
		if self.lst[n] == None:
			self.lst[n] = x
			return self.lst
		else:
			a = self.check_add(n, 1)
			self.lst[a] = x
			return self.lst

	def check_add(self, n, m):
		if self.lst[n + (m ** 2)] == None:
			return n + (m ** 2)
		else:
			return self.check_add(n, m + 1) 

	def get(self, x):
		n = hash(x) % self.len
		if self.lst[n] == x:
			return n
		else:
			a = self.check_get(x, n, 1)
			return a

	def check_get(self, x, n, m):
		if self.lst[n + (m ** 2)] == x:
			return n + (m ** 2)
		else:
			return self.check_get(x, n, m + 1)

h = HashTable(l)