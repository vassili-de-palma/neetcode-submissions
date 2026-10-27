class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        buy = prices[0]

        for i in range(1,n):
            buy = min(buy, prices[i-1])
            ans = max(ans, prices[i] - buy)

        return ans
        