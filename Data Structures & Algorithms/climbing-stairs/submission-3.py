class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None for _ in range(n+1)]
        def rec(n):
            if n <= 1:
                return 1
            if cache[n]: 
                return cache[n]
            ans = rec(n-1) + rec(n-2) 
            cache[n] = ans
            return ans
        return rec(n)
        