class Solution:
    def helper(self,piles,i,j):
        
        if (i,j) in self.computed:
            return self.computed[(i,j)][0],self.computed[(i,j)][1]
        if j-i == 1:
            self.computed[(i,j)] = (max(piles[i],piles[j]),min(piles[i],piles[j]))
            return max(piles[i],piles[j]),min(piles[i],piles[j])

        right_first,right_second = self.helper(piles,i+1,j)
        left_first,left_second = self.helper(piles,i,j-1)
        
        if piles[i] + right_second >= piles[j] + left_second:
            self.computed[(i,j)] = (piles[i] + right_second,right_first)
            return piles[i] + right_second,right_first
        
        self.computed[(i,j)] = (piles[j] + left_second,left_first)
        return piles[j] + left_second,left_first
        
    def stoneGame(self, piles: List[int]) -> bool:
        self.computed = dict()

        first,second = self.helper(piles,0,len(piles)-1)

        if first>second:
            return True
        return False
            
        
