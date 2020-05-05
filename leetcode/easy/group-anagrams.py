class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for str_ in strs:
            sorted_str = str(sorted(str_))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            anagram_dict[sorted_str].append(str_)
            
        return [anagram_dict[str_] for str_ in anagram_dict]
        
