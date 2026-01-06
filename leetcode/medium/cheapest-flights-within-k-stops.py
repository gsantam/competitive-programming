from collections import defaultdict, deque
from queue import PriorityQueue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for flight in flights:
            graph[flight[0]].append([flight[1], flight[2]])

        queue = deque([[src,0,0]])
        distances = {}

        while queue:
            element,distance_cost,distance_stop = queue.popleft()
            if distance_stop>k+1:
                continue
            if element in distances and distances[element]<distance_cost:
                continue
            if element not in distances:
                distances[element] = {}
            distances[element] = distance_cost
            for neigh,price in graph[element]:
                queue.append([neigh,distance_cost+price,distance_stop+1])
        if dst not in distances:
            return -1
        return distances[dst]
