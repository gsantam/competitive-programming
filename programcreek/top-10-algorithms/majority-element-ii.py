from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l =len(nums)
        nums = Counter(nums)
        return[num for num in nums if nums[num]>l//3] 
