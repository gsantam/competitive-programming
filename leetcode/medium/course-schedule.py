from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        not_seen = set([i for i in range(numCourses)])
        graph = defaultdict(lambda: [])
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        while len(not_seen)>0:
            stack = [(set(),not_seen.pop())]
            seen_in_this_round = set()
            while stack:
                element = stack.pop()
                if element[1] in element[0]:
                    return False
                if element[1] in not_seen:
                    not_seen.remove(element[1])
                if element[1] in seen_in_this_round:
                    break
                seen_in_this_round.add(element[1])
                past_in_the_path = element[0].copy()
                past_in_the_path.add(element[1])
                for neigh in graph[element[1]]:
                    stack.append([past_in_the_path,neigh])
        return True
