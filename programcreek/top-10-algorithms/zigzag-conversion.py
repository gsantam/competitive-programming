class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        final_s = ""
        for i in range(numRows):
            j = i
            down = True
            prev_j = -1
            while j<len(s) and len(final_s)<len(s):
                if j!=prev_j:
                    final_s+=s[j]
                prev_j = j
                if down:
                    down = False
                    j+=2*(numRows - i  -1)
                else:
                    down = True
                    j+=i*2
                        
        return final_s
                
                
                
        
