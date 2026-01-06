class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window_length = 0
        left_point = 0
        right_point = -1
        current_characters = set()
        while right_point<len(s)-1:
            if s[right_point+1] not in current_characters:
                right_point+=1
                current_characters.add(s[right_point])
            else:
                current_characters.remove(s[left_point])
                left_point+=1
            max_window_length = max(max_window_length,right_point-left_point+1)
        return max_window_length
