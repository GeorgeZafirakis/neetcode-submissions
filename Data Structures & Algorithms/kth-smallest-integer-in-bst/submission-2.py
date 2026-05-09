# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root)
        return self.arr[k - 1]

    def traverse(self, root: Optional[TreeNode]):
        
        if root is None: return

        self.traverse(root.left)
        self.arr.append(root.val)
        self.traverse(root.right)
