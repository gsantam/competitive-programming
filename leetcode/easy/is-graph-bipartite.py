from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph)==0:
            return True
        graph_dict = dict()
        vertices = set()
        for edge in graph:
            for i in range(len(edge)):
                v1 = edge[i]
                vertices.add(v1)
                if v1 not in graph_dict:
                    graph_dict[v1] = []
                for j in range(i+1,len(edge)):
                    v2 = edge[j]
                    vertices.add(v2)
                    if v2 not in graph_dict:
                        graph_dict[v2] = []
                    graph_dict[v1].append(v2)
                    graph_dict[v2].append(v1)
                    
        while len(vertices)>0:
            seen = dict()
            q = deque([[list(vertices)[0],0]])
            while len(q)>0:
                element = q.popleft()
                current = element[0]
                part = element[1]
                if current in vertices:
                    vertices.remove(current)
                if current in seen:
                    if seen[current] != part:
                        return False
                else:
                    seen[current] = part
                    for vertex in graph[current]:
                        q.append([vertex,(part+1)%2])
                    
        return True
        
        
