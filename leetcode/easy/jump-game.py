class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        done = True
        for i,num in enumerate(nums):
            if i>max_reach:
                done = False
                break
            max_reach = max(max_reach,i+num)
        return done
