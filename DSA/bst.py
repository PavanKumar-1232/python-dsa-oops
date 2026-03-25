##################bst##################################################
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None 
    def insert(self,data):
        if self.root is None:
            self.root=node(data)
            return
        if data<self.root.data:
            if self.root.left is None:
                self.root.left=node(data)
            else:
                self.insert(self.root.left,data)
        else:
            if self.root.right is None:
                self.root.right=node(data)
            else:
                self.insert(self.root.right,data)
    
tree=bst()

data=[9,4,5,6,12,3,14,9,10,0,23,20]            
for i in data:
    tree.insert(i)
