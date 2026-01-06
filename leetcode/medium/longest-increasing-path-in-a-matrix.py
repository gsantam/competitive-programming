class Solution:
    def dfs(self,element):
        if self.longest_so_far[element[0]][element[1]]!=-1:
            return self.longest_so_far[element[0]][element[1]]
        movements = [[0,1],[1,0],[0,-1],[-1,0]]
        length_elements = [0]
        for movement in movements:
            if element[0]+movement[0]>=0 and element[0]+movement[0]<len(self.matrix):
                if element[1]+movement[1]>=0 and element[1]+movement[1]<len(self.matrix[0]):
                    if self.matrix[element[0]+movement[0]][element[1]+movement[1]]>self.matrix[element[0]][element[1]]:
                        length_elements.append(self.dfs([element[0]+movement[0],element[1]+movement[1]]))
        self.longest_so_far[element[0]][element[1]] = max(length_elements)+1
        self.length_longest_path = max(self.length_longest_path,self.longest_so_far[element[0]][element[1]])
        return self.longest_so_far[element[0]][element[1]]
                    


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.longest_so_far = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        self.length_longest_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs([i,j])
        return self.length_longest_path
                        


