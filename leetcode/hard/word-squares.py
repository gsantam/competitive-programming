from collections import defaultdict

class Solution:
    def recurse(self,current):
        if len(current)!=0 and len(current) == len(current[0]):
            self.solutions.add(tuple([x for x in current]))
            return

        word_to_match = []
        for i in range(len(current)):
            word_to_match.append(current[i][len(current)])
        for word in self.memory["".join(word_to_match)]: 
            current_next = current.copy()
            current_next.append(word)
            self.recurse(current_next)
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.solutions = set()
        self.words = words
        self.memory = defaultdict(list)
        for word in words:
            self.memory[''].append(word)
            for i in range(len(word)):
                self.memory[word[0:i+1]].append(word)
        self.recurse([])

        return list([list(x) for x in self.solutions])
