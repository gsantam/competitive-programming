class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0:
            return 0
        if s[0]=='0':
            return 0
            
        if len(s)==1:
            return 1
        
        dynamic = [0 for i in range(len(s))]
        dynamic[0] = 1
        
        if s[1]!='0':
            dynamic[1]+=1
        if int(s[0:2])<=26 and int(s[0:2])>=10:
            dynamic[1] +=1
            
        for i in range(2,len(s)):
            if s[i]!='0':
                dynamic[i] += dynamic[i-1]
            if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>=10:
                dynamic[i]+=dynamic[i-2]
                
        return dynamic[len(s)-1]        
