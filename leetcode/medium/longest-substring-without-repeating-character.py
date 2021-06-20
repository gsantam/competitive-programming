from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters_included = defaultdict(lambda: 0)
        i = -1
        j = 0
        longest = 0
        while i<len(s)-1:
            i+=1
            characters_included[s[i]]+=1
            while characters_included[s[i]]>1:
                characters_included[s[j]]-=1
                j+=1
            longest = max(longest,(i-j)+1)

        return longest
