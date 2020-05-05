from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = Counter(nums)
        seen_so_far = dict()
        total = 0
        if k<0:
            return 0
        if k == 0:
            for num in nums:
                if nums[num]>=2:
                    total+=1
            return total
        
        for num in nums:
            diff_1 = k+num
            diff_2 = num-k
            if diff_1 in seen_so_far:
                total+=seen_so_far[diff_1]
            if diff_2 in seen_so_far and diff_2!=diff_1:
                total+=seen_so_far[diff_2]
            if num not in seen_so_far:
                seen_so_far[num]=0
            seen_so_far[num]+=1
            
        return total
        
