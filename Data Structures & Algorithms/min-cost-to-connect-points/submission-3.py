class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = [(0, points[0][0], points[0][1])]
        visited = set()
        total = 0
        while h:
            cost, xi, yi = heapq.heappop(h)
            if (xi, yi) in visited:
                continue
            visited.add((xi, yi))
            total += cost
            for xj, yj in points:
                if (xj, yj) not in visited:
                    heapq.heappush(h, (abs(xi-xj) + abs(yi-yj), xj, yj))
        return total

        