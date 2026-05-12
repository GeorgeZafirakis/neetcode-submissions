# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node):

            nonlocal res

            # Base Case
            if not node:
                return (0,0) #(height,diam)

            # Recursive Case
            (hl,dl)  = dfs(node.left)
            (hr,dr)  = dfs(node.right)
            diameter = max(dl, dr, hl + hr)
            height   = 1 + max(hl, hr)  
            res = max(res,diameter)
            return (height,diameter)


        dfs(root)
        return res



