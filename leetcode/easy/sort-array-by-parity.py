class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        even = []
        for a in A:
            if a%2==0:
                even.append(a)
            else:
                odds.append(a)
        return even+odds
