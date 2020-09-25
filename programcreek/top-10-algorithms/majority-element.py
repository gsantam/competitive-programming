class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums = sorted(nums)
        sequence_length = 1
        for i,num in enumerate(nums):
            if i!=0 and nums[i-1]==nums[i]:
                sequence_length+=1
            else:
                if sequence_length>len(nums)//2:
                    return nums[i-1]
                sequence_length = 1
        return nums[len(nums)-1]
                
            
        
