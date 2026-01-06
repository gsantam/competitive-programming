class Solution:
    def countSubstrings(self, s: str) -> int:
        n_palindromes = 0
        for i,c in enumerate(s):
            j = 0
            while True:
                if i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:
                    n_palindromes+=1
                else:
                    break
                j+=1
            j = 0
            while True:
                if i-1-j>=0 and i+j<len(s) and s[i-1-j]==s[i+j]:
                    n_palindromes+=1
                else:
                    break
                j+=1
        return n_palindromes
