class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i,num in enumerate(nums):
            if i==0:
                continue
            if nums[i-1]!=nums[i]:
                nums[j] = nums[i]
                j+=1
        return j
