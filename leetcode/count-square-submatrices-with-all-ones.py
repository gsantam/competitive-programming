class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        n_rows = len(matrix)
        if n_rows == 0:
            return 0
        n_cols = len(matrix[0])
        total = 0
        n_squares_by_size = [[0 for j in range(n_cols)] for i in range(n_rows)]
        
        
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j]==1:
                    n_squares_by_size[i][j] = 1
                    if i>=1 and j>=1:
                        if matrix[i-1][j]==1 and matrix[i][j-1]==1 and matrix[i-1][j-1]==1:
                            min_sq = min(n_squares_by_size[i-1][j],n_squares_by_size[i][j-1])
                            min_sq = min(min_sq,n_squares_by_size[i-1][j-1])
                            n_squares_by_size[i][j] = min_sq+1
                    total+= n_squares_by_size[i][j]
                    
        return total
                            
                    
            
        
