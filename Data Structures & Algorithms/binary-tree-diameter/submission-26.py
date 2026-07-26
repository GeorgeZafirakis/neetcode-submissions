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

            if not root:
                return (0,0) # (height, diameter)

            hl, dl = dfs(root.left)
            hr, dr = dfs(root.right)
            h      = 1 + max(hl, hr)
            d      = max(dl, dr, hl + hr)
            return (h,d)


        res = dfs(root)
        return res[1]
        