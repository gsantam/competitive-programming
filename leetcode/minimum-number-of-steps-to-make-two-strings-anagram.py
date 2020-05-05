"""
dict = {"b":1,"-1"}

"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letters = [0 for i in range(30)]
        for i in range(len(s)):
            letters[ord(s[i])-97]+=1
            letters[ord(t[i])-97]-=1
            
        return sum([x for x in letters if x>0])
