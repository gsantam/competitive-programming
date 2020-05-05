"""
[0 1 ]
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumulative = [0 for i in range(len(nums)+1)]
        for i in range(0,len(nums)):
            cumulative[i+1] = cumulative[i] + nums[i]
            
        if len(nums)==1:
            return nums[0]
        max_until_now =  None
        min_until_now =  0
        for i in range(1,len(cumulative)):
            if max_until_now is None:
                max_until_now = cumulative[i]
            else:
                max_until_now = max(cumulative[i] - min_until_now,max_until_now)
            min_until_now = min(min_until_now,cumulative[i])
        return max_until_now
                
            
        
