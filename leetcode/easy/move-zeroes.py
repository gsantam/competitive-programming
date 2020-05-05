class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_zeros = 0
        for i,num in enumerate(nums):
            if num == 0 and n_zeros==0:
                n_zeros+=1
                j = i
            else:
                if n_zeros>0:
                    nums[j] = num
                    nums[i] = 0
                    while nums[j]!=0:
                        j+=1
        return nums
            
        
