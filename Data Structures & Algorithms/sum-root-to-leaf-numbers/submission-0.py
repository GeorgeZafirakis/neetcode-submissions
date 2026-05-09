# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = []
        
        def dfs(node, curSum):

            # Base Case
            if not node:
                return 0 

            curSum = (curSum * 10) + node.val
            if not node.left and not node.right:
                res.append(curSum)

            # Recursive Case
            dfs(node.left,  curSum)
            dfs(node.right, curSum)
        
        dfs(root, 0)

        return sum(res)