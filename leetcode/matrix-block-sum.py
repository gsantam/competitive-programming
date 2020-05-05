class Solution:
    def value_at_position(self,mat,i,j):
        nrows = len(mat)
        ncols = len(mat[0])
        
        if i<0 or i>=nrows:
            return 0
        if j<0 or j>=ncols:
            return 0
        return mat[i][j]
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n_rows = len(mat)
        if n_rows == 0:
            return 0
        n_cols = len(mat[0])
        
        sum_left_top = [[0 for i in range(n_cols)] for j in range(n_rows)]
        block_sum = [[0 for i in range(n_cols)] for j in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                sum_left_top[i][j] = mat[i][j] + self.value_at_position(sum_left_top,i-1,j) + self.value_at_position(sum_left_top,i,j-1) -  self.value_at_position(sum_left_top,i-1,j-1) 
        for i in range(n_rows):
            for j in range(n_cols):
                i__ = min(i+K,n_rows-1)
                j__= min(j+K,n_cols-1)
                
                block_sum[i][j] = sum_left_top[i__][j__] + self.value_at_position(sum_left_top,i-K-1,j-K-1) - self.value_at_position(sum_left_top,i__,j-K-1) - self.value_at_position(sum_left_top,i-K-1,j__)
                
        return block_sum
                
                
                
                
        
