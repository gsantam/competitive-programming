class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0 
        for num in nums:
            if num==0:
                red+=1
            elif num==1:
                white+=1
            elif num==2:
                blue+=1
        for i in range(len(nums)):
            if i<red:
                nums[i] = 0
            elif i>=red+white:
                nums[i] = 2
            else:
                nums[i] = 1
        return nums
