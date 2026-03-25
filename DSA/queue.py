#######################################################queue###############################################
"""class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) == self.size

    def enqueue(self, data):
        if self.is_full():
            print("is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = data


    def dequeue(self):
        if self.rear == -1 or self.front > self.rear:
            print("underflow")
            return
        self.front += 1

    def display(self):
        if self.rear == -1 or self.front > self.rear:
            print("underflow")
            return
        for i in range(self.front, self.rear+1):
            print(self.queue[i], end=" ")

    def peek(self):
        if self.rear == -1 or self.front > self.rear:
            print("underflow")
            return
        print(self.queue[self.front])
pavan = Queue(4)
data = [45,10,7,56]
for val in data:
    pavan.enqueue(val)
pavan.dequeue()
pavan.display()"""
