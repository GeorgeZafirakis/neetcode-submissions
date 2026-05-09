# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Base Case
        if root is None: return 0

        # Recursive Case
        r = self.treeDepth(root.right)
        l = self.treeDepth(root.left)
        d = l + r
        s = max( self.diameterOfBinaryTree(root.right),
                 self.diameterOfBinaryTree(root.left))

        return max(d,s)





    def treeDepth(self, root: Optional[TreeNode]) -> int:

        # Base Case
        if root is None: return 0

        # Recursive Case
        return 1 + max(self.treeDepth(root.left), self.treeDepth(root.right))