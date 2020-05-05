class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        from_ = 0
        longest_so_far = 1
        char_in_interval = {s[0]:0}
        
        for i in range(1,len(s)):
            if s[i] in char_in_interval:
                while from_<char_in_interval[s[i]]+1:
                    if from_ in char_in_interval:
                        del char_in_interval[s[from_]]
                    from_+=1
            char_in_interval[s[i]] = i
            longest_so_far = max(longest_so_far,i-from_+1)
            
        return longest_so_far
