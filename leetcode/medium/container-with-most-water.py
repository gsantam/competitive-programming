class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==1:
            return
        heights = [(height[i],i) for i in range(len(height))]
        heights = sorted(heights,reverse=True)
        leftiest = heights[0]
        rightiest = heights[0]
        longer = -1
        for h,i in heights[1:]:
            longer = max(longer,h*(abs(i-leftiest[1])))
            longer = max(longer,h*(abs(i-rightiest[1])))
            if i<leftiest[1]:
                leftiest=(h,i)
            if i>rightiest[1]:
                rightiest=(h,i)
            

        return longer
