class Solution:            
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
            
        i = 0
        j = 0
        current_prod = 1
        total = 0
        while True:
            if i>=len(nums):
                break

            if nums[i]*current_prod < k:
                current_prod*=nums[i]
                i+=1
                total+=i-j
                
            elif i==j:
                i+=1
                j+=1
            
            else:
                while j<i and nums[i]*current_prod>=k:
                    current_prod = current_prod//nums[j]
                    j+=1
    
        return total
                    
            
            
        
