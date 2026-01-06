class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_ = 0
        for num in nums:
            sum_=sum_^num
        return sum_
