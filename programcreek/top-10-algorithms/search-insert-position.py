class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        
        while i<j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid]>target:
                if j==mid:
                    return j-1
                j = mid
            else:
                if i==mid:
                    return i+1
                i = mid
                
        return (i+j)//2
