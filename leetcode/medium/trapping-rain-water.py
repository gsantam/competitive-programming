class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = []
        max_rights = []
        max_ = 0
        for h in height:
            max_lefts.append(max_)
            max_ = max(max_,h)
        max_ = 0
        rev_height = height.copy()
        rev_height.reverse()
        for h in rev_height:
            max_rights.append(max_)
            max_ = max(max_,h)
        max_rights.reverse()
        total_water = 0
        waters = []
        for i in range(len(height)):
            total_water += max(min(max_rights[i],max_lefts[i])-height[i],0)
        return total_water
