class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        nrow = len(A)
        paths = [[0 for i in range(nrow)] for j in range(nrow)]
        min_path = 10**6
        for i in range(nrow):
            for j in range(nrow):
                if i == 0:
                    paths[i][j] = A[i][j]
                else:
                    j_ = max(j-1,0)
                    j__= min(j+1,nrow-1)
                    min_ = min(paths[i-1][j],paths[i-1][j_])
                    min_ = min(min_,paths[i-1][j__])
                    paths[i][j] = A[i][j] + min_
                if i == nrow-1:
                    min_path = min(min_path,paths[i][j])
                    
        return min_path
        
