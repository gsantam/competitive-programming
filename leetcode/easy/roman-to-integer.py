class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        max_until_now=0 
        total = 0
        for l in reversed(s):
            number = dictionary[l]
            if number>=max_until_now:
                max_until_now = number
                total+=number
            else:
                total-=number
        return total
            
        
