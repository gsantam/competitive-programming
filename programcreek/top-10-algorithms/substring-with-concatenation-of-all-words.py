from collections import Counter

class Solution:
    def find_all(self,a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += 1 # use start += 1 to find overlapping matches
            
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0:
            return []
        
        word_length = len(words[0])
        positions_of_words = dict()
        stack = []
        already = set()
        n_words = len(words)
        words = Counter(words)
        for word in words:
            count = words[word]
            for position in self.find_all(s,word):
                if position not in positions_of_words:
                    positions_of_words[position] =dict()
                    positions_of_words[position][word] = count
                    stack.append([position,position,1,{word:1}])
                
        initial_positions = set()
        while len(stack)>0:
            initial_position,position,total_words,counter = stack.pop()
            if initial_position not in initial_positions:
                if total_words == n_words:
                    initial_positions.add(initial_position)
                    continue
                    
                if (n_words - total_words)*word_length>len(s) - position:
                    continue
                if position + word_length in positions_of_words:
                    for word in positions_of_words[position + word_length]:
                        if word not in counter or counter[word]<positions_of_words[position + word_length][word]:
                            counter_ = counter.copy()
                            if word not in counter_:
                                counter_[word]=0
                            counter_[word]+=1
                            stack.append([initial_position,position+word_length,total_words+1,counter_])
                        
        return initial_positions
                
                
            
            
        
