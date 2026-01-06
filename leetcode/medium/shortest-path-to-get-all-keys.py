from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        queue = deque()
        key_dict = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='@':
                    starting_point = (i,j)
                if ord(grid[i][j])>=ord('a') and ord(grid[i][j])<=ord('z'):
                    key_dict[grid[i][j]] = len(key_dict)
        queue.append((starting_point,tuple([False for i in range(len(key_dict))]),0))
        seen = set()
        while len(queue)>0:
            pos, keys, dis = queue.popleft()
            i,j = pos
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                continue
            if ord(grid[i][j])>=ord('A') and ord(grid[i][j])<=ord('Z') and not keys[key_dict[grid[i][j].lower()]]:
                continue
            if grid[i][j] == '#':
                continue
            new_keys = list(keys).copy()
            if grid[i][j] in key_dict:
                new_keys[key_dict[grid[i][j]]] = True
            if sum(new_keys)==len(key_dict):
                return dis
            new_keys = tuple(new_keys)
            if (pos,new_keys) in seen:
                continue
            seen.add((pos,new_keys))
            for new_pos in ([i+1,j],[i-1,j],[i,j+1],[i,j-1]):
                queue.append((tuple(new_pos),new_keys,dis+1))
        return -1
