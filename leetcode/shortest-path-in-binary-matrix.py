from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        queue.append((1,(0,0)))
        visited = set()
        directions = [(-1+i,-1+j) for i in range(3) for j in range(3) if not (i==1 and j==1)]
        if grid[n-1][n-1]==1:
            return -1
        
        while len(queue)>0:
            element_ = queue.popleft()
            distance = element_[0]
            element = element_[1]
            if element not in visited:
                visited.add(element)
                if element == (n-1,n-1):
                    return distance

                for direction in directions:
                    neigh = (element[0]+direction[0],element[1]+direction[1])
                    if neigh[0]>=0 and neigh[0]<n and  neigh[1]>=0 and neigh[1]<n and grid[element[0]][element[1]]==0:
                        queue.append((distance+1,neigh))
        
        
        return -1
        
