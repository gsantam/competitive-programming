class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        pal = s[0]
        for i in range(len(s)):
            j = 0
            while i+j<len(s) and i-j>=0 and s[i+j]==s[i-j]:
                j+=1
            j-=1
            if 2*j+1>longest:
                longest = 2*j+1
                pal = s[i-j:i+j+1]
        for i in range(len(s)):
            j = 0
            while i+j+1<len(s) and i-j>=0 and s[i+j+1]==s[i-j]:
                j+=1
            j-=1
            if 2*(j+1)>longest:
                longest = 2*j
                pal = s[i-j:i+j+2]
        return pal

