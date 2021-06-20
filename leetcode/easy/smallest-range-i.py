class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A)==1:
            return 0
        max_ = max(A)
        min_ = min(A)
        return max((max_-K) - (min_+K),0)
                
