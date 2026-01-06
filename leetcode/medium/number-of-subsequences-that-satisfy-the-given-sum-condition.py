class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        j = len(nums)-1
        ops = 0
        for i in range(len(nums)):
            if j<i:
                break
            while nums[i] + nums[j]>target and j!=i:
                j-=1
            if nums[i] + nums[j] <= target:
                ops+=2**(j-i)

        return ops%(10**9+7)
