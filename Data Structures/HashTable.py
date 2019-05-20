# -*- coding: utf-8 -*-

#This program creates a simple hash table to store values
l = [0] * 10

class HashTable():

	def __init__(self, lst):
		self.lst = lst
		self.len = len(self.lst)

	def add(self, x):
		n = hash(x) % self.len
		if self.lst[n] == 0:
			self.lst[n] = x
			print self.lst
		else:
			print "No place for", x

	def get(self, x):
		n = hash(x) % self.len
		if self.lst[n] == x:
			print x, "is at index", n
		else:
			print x, "is not present in the list"

h = HashTable(l)