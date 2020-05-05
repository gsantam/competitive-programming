class Solution:
    def helper(self,current,n,k):
        if len(current)==k:
            self.all.append(current)
            return
        
        prev = 0
        if len(current)>0:
            prev = current[-1]
        for i in range(prev+1,n+1):
            self.helper(current+[i],n,k)
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.all = []
        self.helper([],n,k)
        return self.all
