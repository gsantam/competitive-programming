class Solution:
    def countSubstrings(self, s: str) -> int:
        seen_palindromes = set()
        for pal_length in range(1,len(s)+1):
            for i in range(len(s)):
                if i+pal_length<=len(s):
                    seen = False
                    from_ = i
                    to_ = i+pal_length-1
                    current_str = (from_,to_)
                    if pal_length == 1:
                        seen = True
                    elif pal_length == 2 and s[from_]==s[to_]:
                        seen = True
                    else:
                        if s[from_]==s[to_] and (from_+1,to_-1) in seen_palindromes:
                            seen = True                            
                    if seen:
                        seen_palindromes.add(current_str)
        return len(seen_palindromes)
                
                
            


        
        
