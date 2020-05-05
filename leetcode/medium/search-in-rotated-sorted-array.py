class Solution:
    def binary_search(self,nums,i,j,target):
        while j>=i:
            half = (i+j)//2
            if nums[half]==target:
                return half
            if nums[half] < target:
                i = half+1
            else:
                j = half-1
        return -1
        
    def search(self, nums, target):
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1    
        i = 0
        j = len(nums)-1
        
        while j-i>1:
            half = (i+j)//2
            if nums[half] <= nums[i]:
                j = half
            else:
                i = half

        if target>=nums[0] and target<=nums[j-1]:
            return self.binary_search(nums,0,j-1,target)
        elif target>=nums[j] and target<=nums[len(nums)-1]:
            return self.binary_search(nums,j,len(nums)-1,target)
        return -1
        
        
