class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1,len(triangle)):
            for j in range(len(triangle)-i):
                best_child = min(triangle[len(triangle)-i][j],triangle[len(triangle)-i][j+1])
                triangle[len(triangle)-i-1][j] = triangle[len(triangle)-i-1][j] + best_child
                
        return triangle[0][0]
