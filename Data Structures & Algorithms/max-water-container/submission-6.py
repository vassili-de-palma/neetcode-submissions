class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        lo = 0
        hi = n-1
        h = heights

        ans = -1
        while lo < hi:
            A = min(h[lo], h[hi]) * (hi-lo)
            if A > ans: ans = A
            if h[lo] > h[hi]:
                hi = hi - 1
            else:
                lo = lo + 1


        return ans
        
            

            

        