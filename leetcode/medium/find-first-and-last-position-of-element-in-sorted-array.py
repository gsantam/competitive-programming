class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        if nums[0]==target and nums[len(nums)-1]==target:
            return [0,len(nums)-1]
        
        i = 0
        j = len(nums) -1 
        while j-i>=2:

            half = (i+j)//2
            if nums[half]>=target:
                j = half
            else:
                i = half

        if nums[j]!=target and nums[i]!=target:
            return [-1,-1]
        
        if nums[j]==target:
            from_ = j
        if nums[i]==target:
            from_ = i

        i = from_
        j = len(nums) -1 
        while j-i>=2:
            half = (i+j)//2
            if nums[half]<=target:
                i = half
            else:
                j = half    
                
        if nums[i]==target:
            to_ = i
        if nums[j]==target:
            to_ = j
            
        return [from_,to_]
