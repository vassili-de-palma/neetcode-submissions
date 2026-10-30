# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSumNW(self, root: Optional[TreeNode]) -> int:

        ans = float('-inf')
        def rec(node: optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return float('-inf')
            R = rec(node.right)
            L = rec(node.left)
            M = max(node.val, node.val + L, node.val + R, node.val + R + L) 
            ans = max(ans, M)
            return M

        rec(root)
        return ans

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float('-inf')
        def rec(node: optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return float('-inf')
            R = rec(node.right)
            L = rec(node.left)
            M = max(node.val, node.val + L, node.val + R) 
            ans = max(ans, M, node.val + R + L)
            return M

        rec(root)
        return ans
        