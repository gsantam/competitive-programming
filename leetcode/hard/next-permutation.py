
"""
123 -> 231

231 -> 321 -> 

"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        
        biggest = -10**6
        found = False
        for i in range(0,len(nums)):
            from_i = len(nums)-1-i
            if nums[from_i]<biggest:
                found = True
                break
            biggest = nums[from_i]
        
        for j in range(0,len(nums)):
            to_i = len(nums)-1-j
            if nums[to_i]>nums[from_i]:
                break
                
        if not found:
            from_i = -1
        else:     
            swap = nums[from_i]
            nums[from_i] = nums[to_i]
            nums[to_i] = swap
        j = from_i+1
        k = len(nums)-1
        while j<k:
            swap = nums[j]
            nums[j] = nums[k]
            nums[k] = swap
            j+=1
            k-=1
                
