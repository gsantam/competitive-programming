"""
[0 1 ]
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_cumsum_so_far = 0
        cumsum = 0
        max_cumsum =  max(nums)
        for i in range(len(nums)-1):
            cumsum += nums[i]
            min_cumsum_so_far = min(min_cumsum_so_far,cumsum)
            max_cumsum = max(cumsum+ nums[i+1]-min_cumsum_so_far,max_cumsum)
            
        return max_cumsum
