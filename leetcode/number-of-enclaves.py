class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        visited = set()
        numEnclaves = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i,j) not in visited and A[i][j]==1:
                    can_visit_boundary = False
                    stack = [(i,j)]
                    total_lands = 0
                    while len(stack)>0:
                        element = stack.pop()
                        x = element[0]
                        y = element[1]
                        if element not in visited and A[x][y]==1:
                            total_lands+=1
                            visited.add(element)
                            if x+1>=len(A):
                                can_visit_boundary = True
                            else:
                                stack.append((x+1,y))
                            if y+1>=len(A[0]):
                                can_visit_boundary = True
                            else:
                                stack.append((x,y+1))
                            if x-1<0:
                                can_visit_boundary = True
                            else:
                                stack.append((x-1,y))
                            if y-1<0:
                                can_visit_boundary = True
                            else:
                                stack.append((x,y-1))
                    if not can_visit_boundary:
                        numEnclaves+=total_lands
        return numEnclaves
        
