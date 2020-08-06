#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
from collections import deque

def bfs(n, m, edges, s):
    nodes_distance = { i + 1: -1 for i in range(n)}
    connected_nodes = { i + 1: [] for i in range(n)}
    visited_nodes = set()
    for edge in edges:
        connected_nodes[edge[0]].append(edge[1])
        connected_nodes[edge[1]].append(edge[0])
        
    bfs_queue = deque()
    bfs_queue.append((s,0))
    while len(bfs_queue)>0:
        actual_node_ = bfs_queue.popleft()
        actual_node = actual_node_[0]
        distance = actual_node_[1]
        if actual_node not in visited_nodes:
            visited_nodes.add(actual_node)
            nodes_distance[actual_node] = 6*distance
            for neigh_node in connected_nodes[actual_node]:
                bfs_queue.append((neigh_node,distance+1))
                
    nodes_distance = [nodes_distance[x] for x in sorted(list(nodes_distance.keys())) if x!=s]
    return nodes_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

