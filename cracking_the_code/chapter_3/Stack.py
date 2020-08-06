class Stack():
    def __init__(self):
        self.internal_list =[]
        
    def isEmpty(self):
        if len(self.internal_list) == 0:
            return True
        return False
    
    def push(self,item):
        self.internal_list.append(item)
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Empty list")
        else:
            return self.internal_list.pop()
        
stack = Stack()
stack.push(1)
stack.push(2)

print(stack.pop())
                            
