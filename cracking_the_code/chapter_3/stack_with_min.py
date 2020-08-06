class Stack():
    def __init__(self):
        self.internal_list =[]
        self.min_until_the_moment = None
        self.internal_mins = []
        
    def isEmpty(self):
        if len(self.internal_list) == 0:
            return True
        return False
    
    def push(self,item):
        self.internal_list.append(item)
        if self.min_until_the_moment is None:
            self.min_until_the_moment = item
        else:
            if item<self.min_until_the_moment:
                self.min_until_the_moment = item
        self.internal_mins.append(self.min_until_the_moment)
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Empty list")
        else:
            self.min_until_the_moment = self.internal_mins.pop()
            return self.internal_list.pop()
        
    def min(self):
        if self.isEmpty():
            raise Exception("Empty list")
        else:
            return self.min_until_the_moment
