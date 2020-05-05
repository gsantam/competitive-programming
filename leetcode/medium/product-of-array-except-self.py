import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0 for i in range(len(nums))]
        sufixes = [0 for i in range(len(nums))]
        current_prefix = 1
        current_sufix = 1
        
        for i in range(len(nums)):
            current_prefix*= nums[i]
            current_sufix*= nums[len(nums)-i-1]
            
            prefixes[i] = current_prefix
            sufixes[len(nums)-i-1] = current_sufix
            
        result = []
        for i in range(len(nums)):
            mult = 1
            if i>0:
                mult*=prefixes[i-1]
            if i<len(nums)-1:
                mult*=sufixes[i+1]
            result.append(mult)
        return result
            
            
            
            
            
        
        
