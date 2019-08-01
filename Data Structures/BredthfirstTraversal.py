# -*- coding: utf-8 -*-

#This program creates a prints a tree using bredthfirst traversal.

import Queue
class Node:
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None
     
    
class Tree:
    def __init__(self):
        self.head = None
        
    def push(self, x):
        if self.head == None:
            node = Node(x)
            self.head = node
            
        else:
            return self.add(x, self.head)
            
    def add(self, n, node):
        if n >= node.item:
            if node.right_child != None:
                return self.add(n, node.right_child)
            else:
                node.right_child = Node(n)
        else:
            if node.left_child != None:
                return self.add(n, node.left_child)
            else:
                node.left_child = Node(n) 

    def pop(self, x):
        check = self.head
        while check.item != x:
            if x >= check.item:
                check = check.right_child
                
            else:
                check = check.left_child
                
            if check == None:
                return "No such item" 
                
        return self.replace(check)
        
    def search(self, x):
        check = self.head
        
        while check.item != x:
            if x >= check.item:
                check = check.right_child
                
            elif x < check.item:
                check = check.left_child 
            
            if check == None:
                return "No such item"
        
        return check.item

    def bredthfirst_traversal(self, node):
    	list = Queue.Queue(maxsize=100)
    	list.put(node)
    	while list.qsize() > 0:
    		x = list.get()
    		print x.item
    		if x.left_child != None:
	    		list.put(x.left_child)
	    	if x.right_child != None:
	    		list.put(x.right_child)
    		        
tree = Tree()


