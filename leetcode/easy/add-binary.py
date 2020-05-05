class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = ""
        rest = 0
        la = len(a)
        lb = len(b)
        if la==0 or lb==0:
            return "0"
        
        for i in range(max(la,lb)):
            if la-i-1>=0:
                na = int(a[la-i-1])
            else:
                na = 0
                
            if lb-i-1>=0:
                nb = int(b[lb-i-1])
            else:
                nb = 0     
            sum_ = str((na+nb+rest)%2)
            rest = (na+nb+rest)//2
            
            total =  sum_+ total
        if rest==1:
            total =  "1"+ total
            
        return total
        
