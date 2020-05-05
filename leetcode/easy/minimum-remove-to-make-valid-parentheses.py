class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
                
        total_close = 0 
        for i in s:
            if i==")":
                total_close+=1
            
        n_open = 0
        res_s = ""
        seen_closed = 0
        
        for j,i in enumerate(s):
            if i!="(" and i!=")":
                res_s+=i
                
            elif i==")":
                if n_open>0:
                    res_s+=i
                    n_open-=1
                seen_closed+=1
            else:
                if total_close-seen_closed-n_open>0:
                    res_s+=i
                    n_open+=1
        return res_s
