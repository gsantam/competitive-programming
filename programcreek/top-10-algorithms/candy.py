class Solution:
    def recursion(self,pos):
        if self.n_candies[pos] is not None:
            return self.n_candies[pos]
        
        left_candies = 0
        right_candies = 0
        if pos != 0 and self.ratings[pos-1]<self.ratings[pos]:
            left_candies = self.recursion(pos-1)
        right_candies = 0
        if pos != len(self.ratings)-1 and self.ratings[pos+1]<self.ratings[pos]:
            right_candies = self.recursion(pos+1)
        
        my_n_candies = max(left_candies,right_candies) + 1
        self.n_candies[pos] = my_n_candies
        return self.n_candies[pos]
        
    def candy(self, ratings: List[int]) -> int:
        self.ratings = ratings
        self.n_candies = [None for i in range(len(ratings))]
        total_candies = 0
        for pos in range(len(ratings)):
            total_candies+=self.recursion(pos)
        return total_candies
        
