# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return (True,0)

            (bl, hl) = dfs(root.left)  
            (br, hr) = dfs(root.right)
            
            height = 1 + max(hl,hr)
            res = False if abs(hl - hr) > 1 or not bl or not br else True

            return(res,height)          

            

        return dfs(root)[0]

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         def depth(root):

#             if not root:
#                 return 0

#             return 1 + max(depth(root.left), depth(root.right))

#         # Base Case
#         if not root:
#             return True

#         # Recursive Case
#         hl = depth(root.left)
#         hr = depth(root.right)
        
#         if abs(hl - hr) > 1:
#             return False

#         return self.isBalanced(root.left) and self.isBalanced(root.right)

        