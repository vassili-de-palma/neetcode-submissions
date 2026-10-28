from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        @cache
        def rec(i):
            nonlocal ans
            if i >= n:
                return 0
            rob = nums[i] + rec(i+2)
            norob = rec(i+1)
            profit = max(rob, norob)
            ans = max(ans, profit) 
            return profit
        
        rec(0)
        return ans 
        