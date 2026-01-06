class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        array = []
        if len(matrix)==0:
            return []
        def next_(dir_,x,y):
            if dir_ == "r":
                return x,y+1
            if dir_ == "l":
                return x,y-1
            if dir_ == "u":
                return x-1,y
            if dir_ == "d":
                return x+1,y                
        dir_dict = {"r":"d","d":"l","l":"u","u":"r"}
        x = 0
        y = -1
        dir_ = "r"
        for i in range(len(matrix)*len(matrix[0])):
            next_x,next_y = next_(dir_,x,y)
            if next_x<0 or next_x>=len(matrix) or next_y<0 or next_y>=len(matrix[0]) or matrix[next_x][next_y] is None:
                dir_ = dir_dict[dir_]
            x,y = next_(dir_,x,y)
            array.append(matrix[x][y])
            matrix[x][y] = None
        return array
            
