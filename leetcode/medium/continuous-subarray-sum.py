
class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        if len(nums)==0:
            return False
        cumulative_nums = set([0])
        cum = 0
        if k==0:
            for i in range(1,len(nums)):
                if nums[i]==0 and nums[i-1]==0:
                    return True
            return False
        
        for i,num in enumerate(nums):
            cum = (cum+num)%k
            if cum in cumulative_nums and i>=1 and num!=0 and num%k!=0:
                return True
             
            if num%k==0 and i>=1 and nums[i-1]%k==0:
                return True

            cumulative_nums.add(cum)
            
        return False
