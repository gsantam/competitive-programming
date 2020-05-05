class Solution:
    def frequencySort(self, s: str) -> str:
        count = dict()
        for letter in s:
            if letter not in count:
                count[letter] = 0
            count[letter] +=1
            
        count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse = True)}
        final_str = ""
        for k, v in count.items():
            final_str+=k*v
            
        return final_str

