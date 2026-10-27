class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lo = 0
        hi = 1

        ans = 0
        for i in range(1,n):
            buy = min(prices[:i])
            profit = prices[i] - buy
            if profit > ans: 
                ans = profit
        return ans
        