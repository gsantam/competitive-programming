class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        current_length = 0
        for i,char in enumerate(s):
            if s[i]!=" ":
                if i==0 or s[i-1]==" ":
                    current_length=1
                else:
                    current_length+=1
            
        return current_length
