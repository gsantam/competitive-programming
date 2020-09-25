from collections import deque

class Solution:
    def ladderLength(self, start: str, end: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        if end not in dictionary:
            return 0
        
        dictionary.add(start)
        
        generic_graph = dict()
        inverse_generic_graph = dict()
        
        for word_1 in dictionary:
            inverse_generic_graph[word_1] =[]
            for i in range(len(word_1)):
                generic_word = ""
                for j,letter in enumerate(word_1):
                    if i==j:
                        generic_word+="*"
                    else:
                        generic_word+=word_1[j]

                if generic_word not in generic_graph:
                    generic_graph[generic_word] = []
                generic_graph[generic_word].append(word_1)
                inverse_generic_graph[word_1].append(generic_word)
            
        queue = deque([(start,1)])
        seen = set()
        while len(queue) > 0:
            word,depth = queue.popleft()
            if word == end:
                return depth
            if word not in seen:
                seen.add(word)
                           
                for generic_word in inverse_generic_graph[word]:
                    for word_2 in generic_graph[generic_word]:
                        queue.append((word_2,depth+1))
                
        return 0
        
