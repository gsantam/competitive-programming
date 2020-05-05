class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        A = sorted([(a,i) for i,a in enumerate(A)])
        max_ramp = 0
        minimum_i = A[0][1]
        for a, i in A:
            max_ramp = max(max_ramp,i - minimum_i)
            minimum_i = min(minimum_i,i)
            
        return max_ramp
