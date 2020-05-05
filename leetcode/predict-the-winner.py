class Solution:
    def helper(self,i,j,nums):
        if (i,j) in self.cache:
            return self.cache[(i,j)][0],self.cache[(i,j)][1]
        
        if j-i==1:
            self.cache[(i,j)] = (max(nums[i],nums[j]),min(nums[i],nums[j]))
            return max(nums[i],nums[j]),min(nums[i],nums[j])
        
        first_left,second_left = self.helper(i+1,j,nums)
        first_right,second_righ = self.helper(i,j-1,nums)
        
        if nums[i] + second_left >= nums[j] + second_righ:
            self.cache[(i,j)] = (nums[i] + second_left,first_left)
            return nums[i] + second_left,first_left
        self.cache[(i,j)] = (nums[j] + second_righ,first_right)
        return nums[j] + second_righ,first_right

        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.cache = dict()
        if len(nums)==1:
            return True
        
        first,second = self.helper(0,len(nums)-1,nums)
        if first>= second:
            return True
        else:
            return False
        
