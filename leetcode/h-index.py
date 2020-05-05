class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:
            return 0
        citations = sorted(citations,reverse = True)
        for i, citation in enumerate(citations):
            if citation>=i+1:
                pass
            else:
                return i
        
        return len(citations)
        
