
"""
{"a":3,"b":1}
i_1 = 0
i_2 = 1

final_s = "a"
final_s = "ab"
final_s = "aba"

current_i = i_2 = 1

"""
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = Counter(S)
        h = []
        for element in counter:
            heapq.heappush(h,(-counter[element],element))
        final_s = ""
        while len(h)>0:
            el1 = heapq.heappop(h)
            c1 = -el1[0]
            e1 = el1[1]
            if final_s=="" or e1!=final_s[-1]:
                final_s+=e1
                if c1>1:
                    heapq.heappush(h,(-(c1-1),e1))
            else:
                if len(h)==0:
                    return ""
                el2 = heapq.heappop(h)
                c2 = -el2[0]
                e2 = el2[1]     
                final_s+=e2
                if c2>1:
                    heapq.heappush(h,(-(c2-1),e2))
                heapq.heappush(h,(-(c1),e1))
            
        return final_s
            
            
            
        
                    
            
        
        
