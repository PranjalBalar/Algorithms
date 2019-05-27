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
			a = self.check_add(n)
			self.lst[a] = x
			return self.lst

	def check_add(self, n):
		if self.lst[n] == None:
			return n
		else:
			return self.check_add(n + 1) 

	def get(self, x):
		n = hash(x) % self.len
		if self.lst[n] == x:
			return n
		else:
			a = self.check_get(x, n)
			return a

	def check_get(self, x, n):
		if self.lst[n] == x:
			return n
		else:
			return self.check_get(x, n + 1)

h = HashTable(l)