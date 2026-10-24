class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == [[1]]: return 1
        maxarea = 0
        R = len(grid)
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = 1
                    grid[r][c] = 0
                    q = deque([(r,c)])
                    while q:
                        curr = q.popleft()
                        for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nbr = curr[0] + dr
                            nbc = curr[1] + dc
                            if 0 <= nbr < R and 0 <= nbc < C and grid[nbr][nbc] == 1:
                                area += 1
                                grid[nbr][nbc] = 0
                                q.append((nbr,nbc))
                    maxarea = max(maxarea, area)
        
        return maxarea 

        