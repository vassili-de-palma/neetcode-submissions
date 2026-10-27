class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def f(nums):
            if not nums:
                return [[]]
            x = nums[0]
            ans = f(nums[1:])
            return ans + [S + [x] for S in ans]
        
        return f(nums)




        
        