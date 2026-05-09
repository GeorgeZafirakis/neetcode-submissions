# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def dfs(root):

            # Base Case
            if not root:
                return (0,0) # Height, Diameter

            # Recursive Case
            hl, dl = dfs(root.left)
            hr, dr = dfs(root.right)
            h = 1 + max(hl, hr) 
            d = max(dl, dr, hr + hl) 
            return (h,d)

        res = dfs(root)
        return res[1]