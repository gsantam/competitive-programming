class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        if len(nums) <=2:
            return len(nums)
        prev_2 = nums[0]
        prev = nums[1]
        for i, num in enumerate(nums):
            if i<2:
                continue
            if prev!=nums[i] or prev_2!=nums[i]:
                nums[j] = nums[i]
                j+=1
            prev_2 = prev
            prev = num
        return j
            
