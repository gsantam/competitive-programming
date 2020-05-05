class Solution:
    def validPalindrome_(self,s):
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        if len(s)<=2:
            return True
        while i<j:
            if s[i]!=s[j]:
                if i+1==j:
                    return True
                return self.validPalindrome_(s[i:j]) or self.validPalindrome_(s[i+1:j+1])
            else:
                i+=1
                j-=1
        return True
            
        
