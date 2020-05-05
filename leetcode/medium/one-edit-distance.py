class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            swap = s
            s = t
            t = swap
        l1 = len(s)
        l2 = len(t)
        if abs(l1-l2)>1:
            return False
        if l1 == l2:
            dif = 0
            for i in range(l1):
                if s[i]!=t[i]:
                    dif+=1
                    if dif>1:
                        return False 
            if dif == 0:
                return False
        else:
            gap = 0
            for i in range(l1):
                if s[i]!=t[i + gap]:
                    if gap!=0 or s[i]!=t[i+1]:
                        return False
                    gap=1
        return True
        
        
        
