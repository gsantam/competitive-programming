from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n_jumps = 0
        i = 0
        while nums[i]+i<len(nums)-1:
            max_ = 0
            max_pos = -1
            for j in range(1,nums[i]+1):
                if nums[i+j]+j>max_:
                    max_ = nums[i+j]+j
                    max_pos = j
            i = i+max_pos
            n_jumps+=1
        return n_jumps + 1
