class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1 and nums[0] == target:
            return [0,0]
        
        left = 0
        right = len(nums) -1
        while True:
            mid = (left + right) //2
            mid_value = nums[mid]
            
            if mid_value == target:
                break
            if mid == left :
                if nums[right]!=target:
                    return [-1,-1]
                else:
                    mid = right
                    break
            if mid_value < target:
                left = mid
            else:
                right = mid
                
        real_mid = mid
        left = 0
        right = real_mid
        
        print(real_mid)
        while True:
            mid = (left + right) //2
            mid_value = nums[mid]
            
            if mid == 0:
                if nums[left] == target:
                    left_interval = left
                else:
                    left_interval = right
                break
            
            if mid_value!=target :
                if nums[mid+1]==target:
                    left_interval = mid +1
                    break
                else:
                    left = mid
            else:
                right = mid
                
            
        left = real_mid
        right = len(nums)-1
        
        while True:
            mid = (left + right) //2

            mid_value = nums[mid]
            
            if mid==left:
                if nums[right] == target:
                    right_interval = right
                else:
                    right_interval = left
                break
            if mid_value!=target:
                if nums[mid-1] == target:
                    right_interval = mid-1
                    break
                else:
                    right = mid
            else:
                left = mid
        return [left_interval,right_interval]
