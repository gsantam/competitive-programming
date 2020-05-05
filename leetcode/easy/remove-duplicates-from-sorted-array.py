class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return
        prev = nums[0]
        j = 1
        for i in range(1,len(nums)):
            n = nums[i]
            if n!=prev:
                nums[j]=n
                j+=1
            prev = n
            
        return j
