class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacement_s = {}
        replacement_t = {}

        if len(s)!=len(t):
            return False
        
        for i,char in enumerate(s):
            if s[i] not in replacement_s:
                if t[i] in replacement_t:
                    return False
                replacement_s[s[i]] = t[i]
                replacement_t[t[i]] = s[i]
            else:
                if replacement_s[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True

                
                
        
