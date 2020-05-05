class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = -1
        j = -1
        intersection = []
        while i<2*len(A)-1 or j<2*len(B)-1:
            if j>=2*len(B)-1 or (i<2*len(A)-1 and ((A[(i+1)//2][(i+1)%2] < B[(j+1)//2][(j+1)%2]) or (A[(i+1)//2][(i+1)%2] == B[(j+1)//2][(j+1)%2] and (i+1)%2==0 and (j+1)%2==1))):
                if (i+1)%2==1 and (j)%2==0:
                    intersection.append([max(A[i//2][0],B[j//2][0]),A[(i+1)//2][1]])
                i+=1
            else:
                if (j+1)%2==1 and (i)%2==0:
                    intersection.append([max(A[i//2][0],B[j//2][0]),B[(j+1)//2][1]])
                j+=1

            
        return intersection
