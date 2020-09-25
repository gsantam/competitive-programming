class MinStack:

    def __init__(self):
        self.stack = []
        self.min_so_far = None
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        if self.min_so_far is None or x < self.min_so_far:
            self.min_so_far = x
        self.stack.append([x,self.min_so_far])
        
        

    def pop(self) -> None:
        element = self.stack.pop()
        if len(self.stack)>0:
            self.min_so_far = self.getMin()
        else:
            self.min_so_far = None
            


    def top(self) -> int:
        return  self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
