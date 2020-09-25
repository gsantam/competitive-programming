class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cum_nums = [0]
        cum_number = 0
        minimal_length = 10**6
        for num in nums:
            cum_number+=num
            cum_nums.append(cum_number)
            
        """
        [0,2,5,6,8,12,15]   
        """
        
        i = 0
        j = 1
        while i<=len(cum_nums)-1 and j<=len(cum_nums)-1:
            if cum_nums[j] - cum_nums[i]>=s:
                minimal_length = min(minimal_length,j-i)
                
            if i==j:
                j+=1
            elif j==len(cum_nums) - 1:
                i+=1
            elif cum_nums[j] - cum_nums[i]>=s:
                i+=1
            else:
                j+=1
                
                
        
        if minimal_length==10**6:
            return 0
        else:
            return minimal_length
            
            
            
        
