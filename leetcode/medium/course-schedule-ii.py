from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n_prereq = [0 for i in range(numCourses)]
        for from_,to_ in prerequisites:
            graph[to_].append(from_)
            n_prereq[from_]+=1
        without_prereqs = [i for i in range(numCourses) if n_prereq[i]==0]
        if len(without_prereqs)==0:
            return []
        course_list = []
        while len(without_prereqs)>0:
            course = without_prereqs.pop()
            course_list.append(course)
            for neigh in graph[course]:
                n_prereq[neigh]-=1
                if n_prereq[neigh]==0:
                    without_prereqs.append(neigh)
        if len(course_list)==numCourses:
            return course_list
        return []
