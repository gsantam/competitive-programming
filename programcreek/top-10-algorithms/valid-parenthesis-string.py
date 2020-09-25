
"""

( * ) ( * )
"""



class Solution:
    def checkValidString(self, s: str) -> bool:
        n_open = 0
        comodin = []
        s = [char for char in s]
        
        for i,char in enumerate(s):
            if char == "(":
                n_open+=1
            elif char == ")":
                if n_open>0:
                    n_open-=1
                elif len(comodin)>0:
                    pos = comodin.pop()
                    s[pos]=="("
                else:
                    return False
            else:
                comodin.append(i)
                
        comodin = []
        n_close = 0
        
        for i,char in enumerate(reversed(s)):
            if char == ")":
                n_close+=1
            elif char == "(":
                if n_close>0:
                    n_close-=1
                elif len(comodin)>0:
                    pos = comodin.pop()
                    s[pos]=="("
                else:
                    return False
            else:
                comodin.append(i)
                
        
        return True
