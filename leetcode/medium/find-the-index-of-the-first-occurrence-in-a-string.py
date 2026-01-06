class Solution:
    def compute_hash(self,str_,length):
        hash_ = 0
        for i in range(length):
            char = str_[i]
            hash_ += (ord(char) - 97)*(26)**(length-i-1)
        return hash_
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        hash_needle = self.compute_hash(needle,len(needle))
        hash_haystack = self.compute_hash(haystack,len(needle))
        for i in range(len(haystack) - len(needle) + 1):
            if i>0:
                hash_haystack-=(ord(haystack[i-1]) - 97)*(26)**(len(needle)-1)
                hash_haystack*=26
                hash_haystack+=ord(haystack[i+len(needle)-1])-97
            if hash_needle==hash_haystack:
                for j in range(len(needle)):
                    if haystack[i+j]!=needle[j]:
                        break
                    if j==len(needle)-1:
                        return i
        return -1
