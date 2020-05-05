class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        positions = {letter:i for i,letter in enumerate(order)}
        for i in range(1,len(words)):
            word_1 = words[i-1]
            word_2 = words[i]
            j = 0
            while j<min(len(word_1),len(word_2)):
                    if word_1[j]!=word_2[j]:
                        if positions[word_1[j]]>positions[word_2[j]]:
                            return False
                        break
                    j+=1
            if j==min(len(word_1),len(word_2)) and len(word_1)>len(word_2):
                return False
        return True
                
        
