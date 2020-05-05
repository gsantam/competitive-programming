class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        n_rows = len(triangle)
        prev_row = [x for x in triangle[n_rows-1]]
        for i in range(1,n_rows):
            current_row_number = n_rows-1-i
            current_row =[]
            for j in range(len(prev_row)-1):
                current_row.append(triangle[current_row_number][j] + min(prev_row[j],prev_row[j+1]))
            prev_row = current_row.copy()
                                       
        return current_row[0]
                        
                    
                    
                
        
