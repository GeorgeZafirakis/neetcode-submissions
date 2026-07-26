# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root):

            if not root:
                return 0

            return 1 + max(depth(root.left), depth(root.right))

        # Base Case
        if not root:
            return True

        # Recursive Case
        hl = depth(root.left)
        hr = depth(root.right)
        
        if abs(hl - hr) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        