class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Init at 1 the first row and first col 
        # there is only a way for them
        # the other cells will be rewritten in the loop
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]