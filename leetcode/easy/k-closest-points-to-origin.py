import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = sorted([[math.sqrt(point[0]**2+point[1]**2),point[0],point[1]] for point in points])
        
        return [[point[1],point[2]] for point in dis][:K]
        
        
