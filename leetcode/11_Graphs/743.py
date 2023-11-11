from typing import List
from collections import defaultdict
import heapq 

# Basic Dijkstra's algorithm

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v)) # (weight, vertex)

        minHeap = [(0, k)] # (weight, vertex)
        visit = set()
        t = 0

        while minHeap:
            w, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            t = max(t, w)
            # BFS portion

            for w2, v in edges[u]:
                if v not in visit: 
                    heapq.heappush(minHeap, (w + w2, v)) # total path weight, vertex

        return t if len(visit) == n else -1
