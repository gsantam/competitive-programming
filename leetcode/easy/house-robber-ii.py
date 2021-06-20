class Solution:
    
    def rob_(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        best_rob_ending = [0 for i in range(len(nums))]
        best_rob_not_ending = [0 for i in range(len(nums))]

        best_rob_ending[0] = nums[0]
        best_rob_ending[1] = max(nums[0],nums[1])
        best_rob_not_ending[1] = nums[0]

        for i in range(2,len(nums)):
            best_rob_ending[i] = max(best_rob_ending[i-2],best_rob_not_ending[i-1]) + nums[i]
            best_rob_not_ending[i] = max(best_rob_ending[i-1],best_rob_not_ending[i-1])

        return max(best_rob_ending[len(nums)-1],best_rob_not_ending[len(nums)-1])

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_(nums[0:len(nums)-1]),self.rob_(nums[1:len(nums)]))
        
