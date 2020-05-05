class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix)>0:
            cache = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]                             
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cache[i][j] = matrix[i][j]
                if i>0:                                                           
                    cache[i][j] += cache[i-1][j]
                if j>0:                                                           
                    cache[i][j] += cache[i][j-1]
                if i>0 and j>0:
                    cache[i][j] -= cache[i-1][j-1]                                      
            self.cache = cache  
    
                                            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = self.cache[row2][col2]
        if row1>0:
            sum_ -= self.cache[row1-1][col2]
        if col1>0:
            sum_ -= self.cache[row2][col1-1]
        if row1>0 and col1>0:
            sum_+=self.cache[row1-1][col1-1]
        return sum_
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
