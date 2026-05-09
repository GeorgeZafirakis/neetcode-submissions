# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            
            # Base Case
            if root is None: return [True,0]

            # Recursive Case
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]



# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:

#         # Base Case
#         if root is None: return True

#         # Recursive Case
#         h1  = self.treeHeight(root.left)
#         h2  = self.treeHeight(root.right)
#         dif = abs(h1 - h2)

#         if dif > 1:
#             return False

#         return self.isBalanced(root.left) and self.isBalanced(root.right) 

#     def treeHeight(self, root: Optional[TreeNode]) -> bool:

#         # Base Case
#         if root is None: return 0

#         # Recursive Case
#         return 1 + max(self.treeHeight(root.left), 
#                        self.treeHeight(root.right))


        