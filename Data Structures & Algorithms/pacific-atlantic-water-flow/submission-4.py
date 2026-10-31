class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 1: return [[0,0]]
        R, C = len(heights), len(heights[0])
        stack = []

        pacific = [[False]*C for _ in range(R)]
        pacific_coords = [(0,c) for c in range(1,C)] + [(r,0) for r in range(1,R)]
        for r, c in pacific_coords:
            stack.append((r,c))
            while stack:
                cr, cc = stack.pop()
                pacific[cr][cc] = True
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = cr + dr, cc + dc
                    # neighboring condition
                    isNeighbor = (
                        0 <= nr < R and 
                        0 <= nc < C and 
                        heights[nr][nc] >= heights[cr][cc] and 
                        not pacific[nr][nc] 
                    )
                    if isNeighbor:
                        stack.append((nr, nc))
                pacific_coords = [(0,c) for c in range(1,C)] + [(r,0) for r in range(1,R)]
        
        atlantic = [[False]*C for _ in range(R)]
        atlantic_coords = [(R-1,c) for c in range(C)] + [(r,C-1) for r in range(R)]
        for r, c in atlantic_coords:
            stack.append((r,c))
            while stack:
                cr, cc = stack.pop()
                atlantic[cr][cc] = True
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = cr + dr, cc + dc
                    # neighboring condition
                    isNeighbor = (
                        0 <= nr < R and 
                        0 <= nc < C and 
                        heights[nr][nc] >= heights[cr][cc] and 
                        not atlantic[nr][nc] 
                    )
                    if isNeighbor:
                        stack.append((nr, nc))

        ans = []
        for r in range(R):
            for c in range(C):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r,c])
        return ans

 



        