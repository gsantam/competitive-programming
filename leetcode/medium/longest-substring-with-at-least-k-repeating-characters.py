class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if len(s)==0:
            return 0
        
        current_caracters = {s[0]:1}
        max_length = 1
        i = 0
        j = 1
        while j<len(s):
            if s[j] not in current_caracters:
                current_caracters[s[j]]=0
            current_caracters[s[j]]+=1
            while len(current_caracters)>k:
                if s[i] in current_caracters:
                    current_caracters[s[i]]-=1
                if current_caracters[s[i]]==0:
                    del current_caracters[s[i]]
                i+=1
            max_length = max(max_length,j-i+1)
            j+=1
        return max_length
            
            
            
            
        
