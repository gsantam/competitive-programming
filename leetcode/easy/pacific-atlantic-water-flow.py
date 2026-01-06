class Solution:
    def can_flow_to_ocean(self,heights,ocean):
        can_flow = [[False for i in range(len(heights[0]))] for j in range(len(heights))]
        queue = deque()
        seen = set()
        for i in range(len(can_flow)):
            if ocean == "pacific":
                idx_0 = i
                idx_1 = 0

            else:
                idx_0 = i
                idx_1 = len(can_flow[0])-1
            
            queue.append([idx_0,idx_1])
            can_flow[idx_0][idx_1] = True

        for i in range(len(can_flow[0])):
            if ocean == "pacific":
                idx_0 = 0
                idx_1 = i
            else:
                idx_0 = len(can_flow)-1
                idx_1 = i
            queue.append([idx_0,idx_1])
            can_flow[idx_0][idx_1] = True
        neigh_dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            element = queue.popleft()
            if tuple(element) in seen:
                continue
            can_flow[element[0]][element[1]] = True
            seen.add(tuple(element))
            for neigh_dir in neigh_dirs:
                neigh = [element[0]+neigh_dir[0],element[1]+neigh_dir[1]]
                if neigh[0]>=0 and neigh[0]<len(can_flow) and neigh[1]>=0 and neigh[1]<len(can_flow[0]):
                    if heights[neigh[0]][neigh[1]]>=heights[element[0]][element[1]]:
                        queue.append(neigh)
        return can_flow

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_flow_pac = self.can_flow_to_ocean(heights,"pacific")
        can_flow_at = self.can_flow_to_ocean(heights,"atlantic")
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if can_flow_pac[i][j] and can_flow_at[i][j]:
                    result.append([i,j])
        return result
