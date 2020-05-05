from collections import deque
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        to_see = len(t)
        t_letter_positions = dict()
        from_ = None
        total_seen = 0
        for i,char in enumerate(s):
            if char in count_t:
                if char not in t_letter_positions:
                    t_letter_positions[char] = deque()
                if len(t_letter_positions[char])==count_t[char]:
                    t_letter_positions[char].popleft()
                else:
                    total_seen+=1
                t_letter_positions[char].append(i)
                if total_seen==to_see:
                    min_ = min([t_letter_positions[x][0] for x in t_letter_positions])
                    if from_ is None or (i - min_ )<(to_ - from_):
                        from_ = min_
                        to_ = i
        if from_ is None:
            return ""
        return s[from_:to_+1]
                    
                
        
