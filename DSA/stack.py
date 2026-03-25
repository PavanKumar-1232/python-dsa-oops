#######################################################stack##################################################################
"""class Stack:
    def __init__(self,size):
        self.size= size
        self.stack = [0]*size
        self.top = -1
    
    def is_full(self):
        return (self.top+1) == self.size
    
    def push(self, data):
        if self.is_full():
            print("oveflow")
            return 
        self.top+=1
        self.stack[self.top] = data
    
    def pop(self):
        if self.top == -1:
            print("underflow")
            return
        self.top-=1
    
    def display(self):
        if self.top == -1:
            print("underflow")
            return
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=" ")
        
        
    def peek(self):
        if self.top == -1:
            print("underflow")
            return
        print(self.stack[self.top])
pavan = Stack(4)
pavan.push(10)
pavan.push(20)  
pavan.push(30)
pavan.pop()
pavan.display()
print()
pavan.peek()"""