class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = s1
        s = s2
        p_counter = Counter(p)
        a_counter = {char:0 for char in list(p_counter.keys())}

        i = 0
        j = 0
        while i<len(s):
            char = s[i]
            if char not in p_counter:
                a_counter = {char:0 for char in list(p_counter.keys())}
                i+=1
                j=i
            elif a_counter[char]<p_counter[char]:
                a_counter[char]+=1
                if i-j+1==len(p):
                    return True
                i+=1
            else:
                while s[j]!=char:
                    a_counter[s[j]]-=1
                    j+=1
                j+=1
                if i-j+1==len(p):
                    return True
                i+=1
        return False
