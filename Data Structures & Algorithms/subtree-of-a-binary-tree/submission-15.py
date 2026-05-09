# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Base Case
        if root and not subRoot: return True
        if not root and subRoot: return False
        if self.isSameTree(root, subRoot): return True

        # Recursive Case
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            

    def isSameTree(self, p, q):

        # Base Case
        if not p and not q: return True
        if not p and q: return False
        if not q and p: return False
        if p.val != q.val: return False

        # Recursive Case
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)