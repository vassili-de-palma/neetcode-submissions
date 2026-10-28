from functools import cache 

class Solution:
    def rob(self, nums: List[int]) -> int:

        nums1 = nums[1:]
        nums2 = nums[2:-1]
        n1 = len(nums1)
        n2 = len(nums2)

        @cache
        def rec1(i):
            nonlocal ans1
            if i >= n1:
                return 0
            profit = max(nums1[i] + rec1(i+2), rec1(i+1))
            ans1 = max(ans1, profit)
            return profit
        
        @cache
        def rec2(i):
            nonlocal ans2
            if i >= n2:
                return 0
            profit = max(nums2[i] + rec2(i+2), rec2(i+1))
            ans2 = max(ans2, profit)
            return profit
        
        ans1 = 0
        rec1(0)
        ans2 = 0
        rec2(0) 
        return max(ans1, ans2 + nums[0])

        