# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 1
        mydict = {root: root.val}
        def rec(nd):
            nonlocal counter
            ndl = nd.left
            ndr = nd.right
            if ndl:
                mydict[ndl] = max(mydict[nd], ndl.val)
                if ndl.val >= mydict[ndl]:
                    counter += 1
                rec(ndl)
            if ndr:
                mydict[ndr] = max(mydict[nd], ndr.val)
                if ndr.val >= mydict[ndr]:
                    counter += 1
                rec(ndr)
        rec(root)
        return counter
        