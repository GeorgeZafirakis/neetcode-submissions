# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):

            # Base Case
            if not node:
                return 0

            # Recursive Case
            goodnode = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)

            leftSum  = dfs(node.left, maxVal)
            rightSum = dfs(node.right, maxVal)

            res = goodnode + leftSum + rightSum
            return res 


        return dfs(root, root.val)


