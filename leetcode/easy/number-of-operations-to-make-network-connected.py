class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
            
        if len(connections)<n-1:
            return -1
            
        n_connected_components = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                n_connected_components+=1
                stack = [i]
                while len(stack)>0:
                    element = stack.pop()
                    if element not in seen:
                        seen.add(element)
                        for neigh in graph[element]:
                            stack.append(neigh)
                            
        
        return n_connected_components - 1
        
