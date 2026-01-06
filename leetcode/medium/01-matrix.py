class Solution:
    def traverse_right_down(self,mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    self.distances[i][j]=0
                else:
                    if i>0:
                        self.distances[i][j] = min(self.distances[i][j],self.distances[i-1][j]+1)
                    if j>0:
                        self.distances[i][j] = min(self.distances[i][j],self.distances[i][j-1]+1)
    def traverse_left_up(self,mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                i_ = len(mat)-1-i
                j_ = len(mat[0])-1-j
                if mat[i_][j_]==0:
                    self.distances[i_][j_]=0
                else:
                    if i_<len(mat)-1:
                        self.distances[i_][j_] = min(self.distances[i_][j_],self.distances[i_+1][j_]+1)
                    if j_<len(mat[0])-1:
                        self.distances[i_][j_] = min(self.distances[i_][j_],self.distances[i_][j_+1]+1)

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.distances = [[10**6 for i in range(len(mat[0]))] for j in range(len(mat))]
        self.traverse_right_down(mat)
        self.traverse_left_up(mat)
        return self.distances
