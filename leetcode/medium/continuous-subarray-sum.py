class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_nums = [0 for i in range(len(nums)+1)]
        
        for i,num in enumerate(nums):
            cum_nums[i+1] = cum_nums[i]+ num
        total = 0
        my_dict = dict()
        
        for i in range(len(cum_nums)):
            if -(k-cum_nums[i]) in my_dict:
                total+=my_dict[-(k-cum_nums[i])]
            if cum_nums[i] not in my_dict:
                my_dict[cum_nums[i]] = 0
            my_dict[cum_nums[i]]+=1
        return total
                
        
                    
        
