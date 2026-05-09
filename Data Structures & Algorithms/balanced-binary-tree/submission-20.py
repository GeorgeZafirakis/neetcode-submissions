# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            # Base Case
            if not node:
                return (True,0)

            # Recursive Case
            (bl,hl) = dfs(node.left)
            (br,hr) = dfs(node.right)

            height = 1 + max(hl,hr)
            return (bl and br and abs(hl - hr) <= 1, height)
            

        return dfs(root)[0]