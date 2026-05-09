# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # Base Case
        if not root: return None
        if p and not q: return None
        if q and not p: return None
        if not p and not q: return root

        # Recursive Case
        if  p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        else:
            return root








