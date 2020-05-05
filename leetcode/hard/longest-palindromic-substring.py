class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        
        long_from = 0
        long_to = 1
        for i in range(len(s)):
            j = i
            k = i
            while (j+1)<len(s) and (k-1)>=0 and s[j+1] == s[k-1]:
                j+=1
                k-=1
            if (j-k+1)>(long_to - long_from):
                long_from = k
                long_to = j+1
                
        for i in range(len(s)):
            j = i
            k = i+1
            one = False
            while (j+1)<len(s) and (k-1)>=0 and s[j+1] == s[k-1]:
                j+=1
                k-=1
                
            if (j-k+1)>(long_to - long_from):
                long_from = k
                long_to = j+1
                
        return s[long_from:long_to]
                
            
                
