# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, node: TreeNode, maxVal: int) -> int:

        # Base Case
        if node is None: return 0

        # Recursive Case
        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        res += self.dfs(node.left, maxVal)
        res += self.dfs(node.right, maxVal)
        return res


