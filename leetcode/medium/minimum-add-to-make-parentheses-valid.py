class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n_open = 0
        n_to_add = 0
        for char in s:
            if char == "(":
                n_open+=1
            else:
                if n_open>0:
                    n_open-=1
                else:
                    n_to_add+=1
        n_to_add+=n_open
        return n_to_add
