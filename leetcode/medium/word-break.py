class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        indices = [False for i in range(len(s)+1)]
        indices[0] = True
        for i in range(len(s)):
            if indices[i] == False:
                continue
            current_word = ""
            for j,letter in enumerate(s):
                if j>=i:
                    current_word+=letter
                    if current_word in wordDict:
                        indices[j+1] = True
        print(indices)
        return indices[len(indices)-1] == True
