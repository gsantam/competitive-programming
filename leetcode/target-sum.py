

class Solution:
    def get_pos_from_n(self,n):
        return self.max_sum + n
        
    def get_n_from_pos(self,pos):
        return pos - self.max_sum    
            
    
    def findTargetSumWays(self, nums, S) :
        max_sum = sum(nums)
        self.max_sum = max_sum
        matrix = [[0 for i in range(3*max_sum+2)] for j in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            if i == 0:
                matrix[0][self.get_pos_from_n(num)] += 1
                matrix[0][self.get_pos_from_n(-num)] += 1
            else:
                for j in range(2*max_sum+1):
                    n = self.get_n_from_pos(j)
                    matrix[i][self.get_pos_from_n(n + num)] +=  matrix[i-1][j]
                    matrix[i][self.get_pos_from_n(n - num)] +=  matrix[i-1][j]
                    
        if self.get_pos_from_n(S)<0 or self.get_pos_from_n(S)>=2*max_sum+2:
            return 0
        return matrix[len(nums)-1][self.get_pos_from_n(S)]


        
