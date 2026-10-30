from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = bisect_left(range(m * n), target, key=lambda i: matrix[i // n][i % n])
        return i < m * n and matrix[i // n][i % n] == target