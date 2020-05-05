from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        a_counter = {char:0 for char in list(p_counter.keys())}

        i = 0
        j = 0
        all_indexes = []
        while i<len(s):
            char = s[i]
            if char not in p_counter:
                a_counter = {char:0 for char in list(p_counter.keys())}
                i+=1
                j=i
            elif a_counter[char]<p_counter[char]:
                a_counter[char]+=1
                if i-j+1==len(p):
                    all_indexes.append(j)
                i+=1
            else:
                while s[j]!=char:
                    a_counter[s[j]]-=1
                    j+=1
                j+=1
                if i-j+1==len(p):
                    all_indexes.append(j)
                i+=1
                
        
        return all_indexes
