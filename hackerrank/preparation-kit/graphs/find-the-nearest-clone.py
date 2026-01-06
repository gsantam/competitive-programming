#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(lambda: [])
    for i in range(len(graph_from)):
        graph[graph_from[i]-1].append(graph_to[i]-1)
        graph[graph_to[i]-1].append(graph_from[i]-1)
    queue = deque()
    for i in range(graph_nodes):
        if ids[i]==val:
            queue.append([i,i,0])
    seen = {}
    while len(queue)!=0:
        root,element,dis = queue.popleft()
        if element in seen:
            root_,dis_ = seen[element]
            if root_==root:
                continue
            return dis_+dis
        seen[element] = [root,dis]
        for neigh in graph[element]:
            queue.append([root,neigh,dis+1])        
    return -1

    
    # solve here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

