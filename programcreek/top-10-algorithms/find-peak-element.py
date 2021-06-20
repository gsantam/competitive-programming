class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        left = 0
        right = len(nums)-1
        
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        
        while True:
            mid = (left + right) //2
            if mid==0:
                left_nums = -10**10
            else:
                left_nums = nums[mid-1]
                
            if mid ==len(nums)-1:
                right_nums = -10**10
            else:
                right_nums = nums[mid+1]
                
            if nums[mid]>left_nums and nums[mid]>right_nums:
                return mid
            
            if nums[mid] > left_nums:
                left = mid
            else:
                if nums[mid] < right_nums:
                    left = mid
                else:
                    right = mid
                    
                
                
            
        
