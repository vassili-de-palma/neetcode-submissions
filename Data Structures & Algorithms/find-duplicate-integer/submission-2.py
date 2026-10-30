class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()
        for x in nums:
            if x in myset:
                return x
            myset.add(x)
        
        