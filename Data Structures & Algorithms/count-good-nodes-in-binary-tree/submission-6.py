# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = [0]

        def dfs(node, maxVal, res):

            if not node:
                return (node, maxVal, res)

            if node.val >= maxVal:
                res[0] += 1
                maxVal = node.val

            dfs(node.left,  maxVal, res)
            dfs(node.right, maxVal, res)
            return (node,   maxVal, res)

        dfs(root, -1000, res)
        return res[0]
        