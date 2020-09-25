from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = -1
        min_length_of_substring = 10**10
        min_substring = ""
        characters_in_current_substring = dict()
        chars_in_t = Counter(t)
        
        while left < len(s):
            valid = True
            for char in chars_in_t:
                if char not in characters_in_current_substring or characters_in_current_substring[char] < chars_in_t[char]:
                    valid = False
            if right>=len(s)-1 or valid:
                    if valid:
                        if right - left + 1<min_length_of_substring:
                            min_length_of_substring = right - left + 1
                            min_substring = s[left:right+1]

                        if min_length_of_substring==1:
                            return min_substring
                    characters_in_current_substring[s[left]] -=1
                    if characters_in_current_substring[s[left]] == 0 :
                        del characters_in_current_substring[s[left]]
                    left+=1

            else:
                right = right+1
                if s[right] not in characters_in_current_substring:
                    characters_in_current_substring[s[right]] = 0
                characters_in_current_substring[s[right]] +=1
                   
        return min_substring
                
            
            
                

                    
                
        
