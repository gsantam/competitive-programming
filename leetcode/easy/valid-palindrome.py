class Solution:
    
    def check_letter(self,char):
        if (char>="a" and char<="z") or (char>="0" and char<="9"):
            return True
        return False
    
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if not self.check_letter(s[i].lower()):
                i+=1
            elif not self.check_letter(s[j].lower()):
                j-=1    
            elif  s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1
                j-=1
            
        return True
        
