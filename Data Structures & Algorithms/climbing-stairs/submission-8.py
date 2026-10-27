from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache 
        def rec(n):
            if n <= 1:
                return 1
            ans = rec(n-1) + rec(n-2) 
            return ans
        return rec(n)
        