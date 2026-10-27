class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort() # O(nlogn)


        def sumfrq(nums, frq):
            return sum([nums[i]*frq[i] for i in range(n)])

        ans = []
        def backtrack(frq, start):
            if sumfrq(nums, frq) > target: 
                return
            for j in range(start, n):
                nfrq = frq[:]
                nfrq[j] += 1
                s = sumfrq(nums, nfrq)
                if s == target:
                    ans.append([nums[i] for i, c in enumerate(nfrq) for _ in range(c)])
                    return
                elif s < target:
                    backtrack(nfrq, j)
                    
                

        backtrack([0]*n, 0)
        return ans
        


        