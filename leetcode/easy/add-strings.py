class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = 0
        l1 = len(num1)
        l2 = len(num2)
        rest = 0
        total_sum = 0
        while l1-1-i>=0 or l2-1-i>=0:
            sum_ = rest
            if  l1-1-i>=0:
                sum_+=int(num1[l1-1-i])
            if l2-1-i>=0:
                sum_+=int(num2[l2-1-i])
                
            rest = sum_//10
            sum_ = sum_%10
            total_sum+=sum_*(10**i)
            i+=1

        if rest!=0:
            total_sum+=rest*(10**i)
            
        return str(total_sum)
        
            
        
