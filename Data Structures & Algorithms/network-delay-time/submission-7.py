class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for ui, vi, ti in times:
            graph[ui-1].append((vi-1,ti))
        
        src = k-1
        dist = [float('inf')] * n
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        ans = max(dist)
        return ans if ans < float('inf') else -1
        


        

        