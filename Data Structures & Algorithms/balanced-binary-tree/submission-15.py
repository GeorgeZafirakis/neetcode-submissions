# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        flag = True
        
        def dfs(node):

            nonlocal flag

            if not node:
                return (True, 0)

            (bl, hl) = dfs(node.left)
            (br, hr) = dfs(node.right)

            height = 1 + max(hl, hr)

            if abs(hl - hr) > 1:
                flag = False

            return (True, height)

            
        dfs(root)
        return flag