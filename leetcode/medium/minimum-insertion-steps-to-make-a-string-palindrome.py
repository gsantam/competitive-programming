class Solution:
    def minInsertions(self, s: str) -> int:
        if len(s)==0:
            return
        current_candidates = [0 for i in range(len(s))]
        best = len(s)-1
        for i,let in enumerate(s):
            j = len(s)-1
            carrying_candidates = 0
            while j>i:
                current_candidates_pos = current_candidates[j]
                if s[j]==let:
                    current_candidates[j]=max(current_candidates[j],carrying_candidates+1)
                carrying_candidates=max(carrying_candidates,current_candidates_pos)
                if s[j]==let:
                    current_candidates[j] = max(1,current_candidates[j])
                    if j>i+1:
                        best = min(best,len(s) - 2* current_candidates[j] - 1)
                    else:
                        best = min(best,len(s) - 2* current_candidates[j] )
                j-=1
        return best
