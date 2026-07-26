# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left_val, node, right_val):

            # Base Case
            if not node:
                return True

            if left_val >= node.val or right_val <= node.val:
                return False

            # Recursive Case
            return dfs(left_val,node.left,node.val) and dfs(node.val,node.right,right_val)

        return dfs(-1001, root, 1001) 





