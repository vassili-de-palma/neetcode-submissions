# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            q = deque([(root, 0)]) 
        else:
            return []

        while q:
            node, level = q.popleft()
            if level == len(ans):
                ans.append(node.val)
            if node.right:
                q.append((node.right, level+1)) 
            if node.left:
                q.append((node.left, level+1)) 
        return ans
            


        