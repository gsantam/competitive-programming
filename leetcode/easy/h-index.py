class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations,reverse = True)
        n = len(citations)
        for i,citation in enumerate(citations):
            if not (citation>=i+1):
                return i
            
        return n
