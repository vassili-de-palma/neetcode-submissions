class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [(x*x + y*y, x, y) for x,y in points]
        heapq.heapify(h)
        ans = []
        for i in range(k):
            d, x, y = heapq.heappop(h)
            ans.append([x, y])
        return ans

        