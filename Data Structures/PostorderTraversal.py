# -*- coding: utf-8 -*-

#This program prints a tree using postorder traversal
 
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
                return
        else:
            if node.left_child != None:
                return self.add(n, node.left_child)
            else:
                node.left_child = Node(n)
                return
            
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
        
    def replace(self, x):
        
        if x.right_child != None:
            x.item = x.right_child.item
            return self.replace(x.right_child)
        
        else:
            x.item = None
            return
        
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

    def postorder_traversal(self, node):
        if node.left_child != None:
            self.postorder_traversal(node.left_child)
        if node.right_child != None:
            self.postorder_traversal(node.right_child)
        print node.item
        return
        
tree = Tree()
tree.push(9)
tree.push(10)
tree.push(7)
tree.push(12)
tree.push(5)
tree.push(2)
tree.postorder_traversal(tree.head)


