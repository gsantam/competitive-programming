class Solution:
    def findLadders(self, start: str, end: str, dictionary: List[str]) -> List[List[str]]:
        
        
        
        dictionary = set(dictionary)
        if end not in dictionary:
            return []

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
                
                
                
        
        queue = deque([[start]])
        shortest = dict()
        paths = []
        while len(queue) > 0:
            seq = queue.popleft()
            word = seq[-1]

            if word not in shortest or shortest[word]>=len(seq):
                if word == end:
                    paths.append(seq)
                shortest[word] = len(seq)
                for generic_word in inverse_generic_graph[word]:
                    for word_2 in generic_graph[generic_word]:
                        queue.append(seq+[word_2])
        return paths
        
