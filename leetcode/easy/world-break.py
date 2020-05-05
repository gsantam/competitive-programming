class Solution:
    def helper(self,world):
        if world in self.memo:
            return self.memo[world]
        if world == "":
            self.memo[""] = True
            return True
        left = ""
        for i in range(len(world)):
            left+=world[i]
            if left in self.worlds:
                if self.helper(world[i+1:]):
                    self.memo[world] = True
                    return True 
        self.memo[world] = False
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = dict()
        if s=="" and "" not in wordDict:
            return False
        self.worlds = set(wordDict)
        return self.helper(s)
        
