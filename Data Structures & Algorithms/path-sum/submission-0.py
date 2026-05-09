# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        res = []

        def dfs(root, curSum):
        
            # Base Case
            if not root:
                return

            curSum += root.val
            if not root.left and not root.right:
                res.append(curSum)
                return
            
            # Recursive Case
            dfs(root.left, curSum)
            dfs(root.right, curSum)

        dfs(root, 0)

        return targetSum in res





