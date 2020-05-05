class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_row = len(matrix)
        if n_row==0:
            return 0
        n_col = len(matrix[0])

        max_size = 0
        for i in range(n_row):
            for j in range(n_col):
                size = 1
                stop = False
                while not stop:
                    for k in range(size):
                        if i+size-1 < n_row and j+k < n_col and matrix[i+size-1][j+k] == "1" and j+size-1<n_col and i+k<n_row and  matrix[i+k][j+size-1] == "1":
                            pass
                        else:
                            stop = True
                            break
                    if not stop:
                        size+=1
                max_size  = max(max_size,size-1)      
        return max_size**2
                
                            
                
        
