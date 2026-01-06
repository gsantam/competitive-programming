class Solution:
    def largestRectangleArea_(self, heights: List[int], reverse = False) -> int:
        stack = []
        areas = heights.copy()
        for i,h in enumerate(heights):
            element = None
            while len(stack)>0:
                element = stack.pop()
                if element[0] <= h:
                    stack.append(element)
                    break
                else:
                    h_2 = element[0]
                    i_2 = element[1]
                    areas[i_2] = max(areas[i_2],h_2*(i-i_2))
            
            stack.append([h,i])

        while len(stack)>0:
            h_2,i_2 = stack.pop()
            areas[i_2] = max(areas[i_2],h_2*(i-i_2+1))
        return areas

    def largestRectangleArea(self, heights: List[int]):
        areas_right = self.largestRectangleArea_(heights)
        areas_left = list(reversed(self.largestRectangleArea_(list(reversed(heights)))))
        max_area = [areas_right[i]+ areas_left[i]-heights[i] for i in range(len(heights))]
        return max(max_area)
