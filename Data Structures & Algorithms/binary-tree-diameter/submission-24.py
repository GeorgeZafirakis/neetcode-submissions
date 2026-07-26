# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def depth(root):

            if not root:
                return 0

            return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return 0

        leftDepth  = depth(root.left)
        rightDepth = depth(root.right)
        diameter   = leftDepth + rightDepth 
        res = max(res, diameter)
        res = max(res, self.diameterOfBinaryTree(root.left))
        res = max(res, self.diameterOfBinaryTree(root.right))

        return res

        