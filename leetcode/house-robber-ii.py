class Solution:
    
    def rob_row(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp  = [0 for i in range(len(nums))]
        dp_taken = [False for i in range(len(nums))]
        dp[0] = nums[0]
        dp_taken[0] = True
        if nums[1]>nums[0]:
            dp[1] = nums[1]
            dp_taken[1] = True
        else:
            dp[1] = nums[0]
            dp_taken[1] = False

        for i in range(2,len(nums)):
            if dp_taken[i-1]==False:
                dp[i] = dp[i-1] +nums[i]
                dp_taken[i] = True
            else:
                if dp[i-2] + nums[i] > dp[i-1]:
                    dp[i] = dp[i-2] + nums[i]
                    dp_taken[i] = True
                else:
                    dp[i] = dp[i-1]
                    dp_taken[i] = False
        return dp[len(nums)-1]    
    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_row(nums[0:len(nums)-1]),self.rob_row(nums[1:len(nums)]))
        
