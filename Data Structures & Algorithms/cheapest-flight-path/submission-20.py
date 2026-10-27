class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))

        pq = [(0,src,0)]
        best_stops = [float('inf')] * n
        dist = [float('inf')] * n
        dist[src] = 0
        

        while pq:
            d, u, stops = heapq.heappop(pq)

            if u == dst:    # early exit
                return d

            if stops > k or stops >= best_stops[u]: # laxy deletion
                continue 

            best_stops[u] = stops

            for v, w in adj[u]:
                nd = d + w
                nstops = stops + 1
                heapq.heappush(pq, (nd, v, nstops))  
        
        return -1

