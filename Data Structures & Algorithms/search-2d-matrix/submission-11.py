from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][-1] < target:
                lo = mid + 1
            else:
                hi = mid
        k = bisect_left(matrix[lo], target)

        if k < len(matrix[lo]) and matrix[lo][k] == target:
            return True 

        return False
      