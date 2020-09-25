

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i,num in enumerate(nums):
            if num!=0:
                nums[j]=num
                j+=1
        if j==0:
            return nums
        
        for i in range(len(nums) - j):
            nums[j+i] = 0
        return nums
                
            
        
