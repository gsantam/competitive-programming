class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumsum = [0 for i in range(len(nums)+1)]
        min_so_far = 0
        largest = -10**10
        for i,num in enumerate(nums):
            cumsum[i+1] = num + cumsum[i]
            largest= max(largest,cumsum[i+1] -min_so_far )
            min_so_far= min(min_so_far,cumsum[i+1] )
        return largest
