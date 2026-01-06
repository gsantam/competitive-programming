class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)
        minimum = 10**10
        nums = sorted(nums)
        for i in range(1,len(nums)):
            new_nums_low = min(min_+k,nums[i]-k)
            new_nums_high = max(max_-k,nums[i-1]+k)
            if new_nums_high>=new_nums_low:
                minimum = min(minimum,new_nums_high-new_nums_low)
        minimum = min(minimum,max_-min_)
        return minimum
