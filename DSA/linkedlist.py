####################################linked list#########################################
"""class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_start(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_at_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return 
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=newnode   
    def display(self):
        curr=self.head
        if curr is None:
            print("empty")
            return  
        while curr.next:
            print(curr.data,end="->")
            curr=curr.next
    def delete_at_start(self):
        if self.head is None:
            print("empty")
            return 
        self.head=self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("empty")
            return
        if self.head.next is None:
            self.head=None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next     
        curr.next = None  
    def position_insertion(self,data,pos):
        if pos==0:
            self.insert_at_start(data)
            return
        newnode=node(data)
        curr = self.head
        for i in range(pos-1):
            if curr.next is None:
                break
            curr = curr.next
        newnode.next = curr.next
        curr.next = newnode    
    def search(self,key):
        curr=self.head
        while curr:
            if curr.data==key:
                return True
            curr=curr.next
        return False    
    def position_delection(self,pos):
        if self.head is None:
            print("empty")
            return
        if pos==0:
            self.head=self.head.next
            return
        curr=self.head
        for i in range(pos-1):
            if curr.next is None:
                print("position out of range")
                return
            curr=curr.next
        curr.next=curr.next.next"""