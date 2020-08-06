"""
enqueue

1
2
3
stack1 = [1,2,3]
stack2 = []

print

stack1 = []
stack2 = [3,2,1]

1

enqueue

4
stack1 = [4]
stack2 = [3,2,1]

dequeue

stack1 = [4]
stack2 = [3,2]

1

enqueue

4

stack1 = [4,5]
stack2 = [3,2]

dequeue


stack1 = [4,5]
stack2 = [3]

2

dequeue

stack1 = [4,5]
stack2 = []

3

dequeue

stack1 = []
stack2 = [5]

4



"""


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def invert_queues(self):
        if len(self.stack2) == 0:
            while len(self.stack1) !=0:
                self.stack2.append(self.stack1.pop())
    
    def enqueue(self,element):
        if element is not None:
            self.stack1.append(element)
            
    def dequeue(self):
        self.invert_queues()
                
        if len(self.stack2)>0:
            return self.stack2.pop()
        
    def print_from(self):
        self.invert_queues()
        
        if len(self.stack2)>0:
            print(self.stack2[-1])
            
    
queue = Queue()
q = int(input())

for i in range(q):
    query = input().strip()
    if len(query.split(" ")) == 2:
        element = int(query.split(" ")[1])
        queue.enqueue(element)
    else:
        query_type = int(query)
        if query_type == 2:
            queue.dequeue()
        if query_type==3:
            queue.print_from()
