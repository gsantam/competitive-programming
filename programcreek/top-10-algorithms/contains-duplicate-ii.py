class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:        
        nums_in_window = dict()            
        for i in range(len(nums)):
            if i-k-1>=0:
                nums_in_window[nums[i-k-1]]-=1
            if nums[i] not in nums_in_window:
                nums_in_window[nums[i]]=0
            nums_in_window[nums[i]]+=1
            
            if  nums_in_window[nums[i]]>=2:
                return True
                
        return False
