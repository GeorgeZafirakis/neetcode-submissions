# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):

            # Base Case
            if not root:
                return (0,0) # (Height, Diameter)

            # Recursive Case
            h_left, d_left   = dfs(root.left)
            h_right, d_right = dfs(root.right) 

            height = 1 + max(h_left, h_right)
            diam   = max(d_right, d_left, h_left + h_right)

            return (height, diam)

        return dfs(root)[1]