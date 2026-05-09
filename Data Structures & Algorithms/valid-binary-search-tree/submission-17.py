# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left, cur, right):

            # Base Case
            if not cur:
                return True

            if left >= cur.val or right <= cur.val:
                return False

            # Recursive Case
            return dfs(left, cur.left, cur.val) and dfs(cur.val, cur.right, right )

        return dfs(float("-inf"), root, float("inf"))

