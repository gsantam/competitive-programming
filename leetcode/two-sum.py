class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = dict()
        for i,num in enumerate(nums):
            if target - num in already_seen:
                return [already_seen[target- num],i]
            already_seen[num] = i
                
        
