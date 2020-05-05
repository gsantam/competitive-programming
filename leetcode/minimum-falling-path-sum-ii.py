class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        nrow = len(A)
        if nrow == 1:
            return A[0][0]
        paths = [[0 for i in range(nrow)] for j in range(nrow)]
        min_path = 10**6
        row_sum = [sum(row) for row in A]
        for i in range(nrow):
            if i !=0 :
                row = sorted([(element,pos) for pos,element in enumerate(paths[i-1])])
            for j in range(nrow):
                if i == 0:
                    paths[i][j] = A[i][j]
                else:
                    if j!=row[0][1]:
                        paths[i][j] = A[i][j] + row[0][0]
                    else:
                        paths[i][j] = A[i][j] + row[1][0]
                if i == nrow-1:
                    min_path = min(min_path,paths[i][j])

        return min_path
