class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A = sorted(A)
        n_moves = 0
        if len(A)<=1:
            return 0
        prev = A[0]
        for i in range(1,len(A)):
            if A[i]>prev:
                prev = A[i]
            else:
                n_moves += (prev-A[i]+1)
                prev = prev +1
                
        return n_moves
        
