"""
n is the first
consider n+k

1 2 4

n = 1
k = 3
n+k=4

2 -> n+k = 5
4 -> n+k = 6


"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = nums[0]
        n_k = n + k 
        for i in range(1,len(nums)):
            if nums[i]<=n_k:
                n_k+=1
            else:
                return n_k
        return n_k
