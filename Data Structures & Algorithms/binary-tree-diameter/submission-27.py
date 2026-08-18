# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if not node: return (0,0)

            hl,dl    = dfs(node.left)
            hr,dr    = dfs(node.right)
            height   = 1  + max(hl,hr)
            diam     = max(dl, dr, hl + hr) 
            return (height, diam)

        return dfs(root)[1]