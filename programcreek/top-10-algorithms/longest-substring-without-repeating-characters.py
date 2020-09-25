
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left_ =0
        right_ = 0
        longest_so_far = 1
        char_in_current_substring = set()
        
        while left_<len(s) and right_<len(s):
            if s[right_] in char_in_current_substring:
                while s[left_]!=s[right_]:
                    char_in_current_substring.remove(s[left_])
                    left_+=1
                left_+=1
            char_in_current_substring.add(s[right_])
            longest_so_far  = max(right_-left_+1,longest_so_far)
            right_+=1    
            
            
        return longest_so_far
            
