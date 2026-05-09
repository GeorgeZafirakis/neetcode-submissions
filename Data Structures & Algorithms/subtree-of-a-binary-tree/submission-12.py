# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(node1, node2):

            # Base Case
            if not node1 and not node2: return True
            if node1 and not node2: return False
            if not node1 and node2: return False
            if node1 and node2 and node1.val != node2.val: return False

            # Recursive Case
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        # Base Case
        if root and not subRoot:
            return True

        if not root and subRoot:
            return False

        # Recursive Case
        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        




