# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):

            # Base Case
            if node is None: return 0
            # Recursive Case
            return 1 + max(depth(node.left), depth(node.right))

        # Base Case
        if root is None:
            return True

        d1 = depth(root.left)
        d2 = depth(root.right)
        if abs(d1 - d2) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)