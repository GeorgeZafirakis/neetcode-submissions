# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        self.traverse(root, res)
        print(res)

        for i in range(len(res) - 1):
            if res[i+1] <= res[i]:
                return False
        return True
    
    def traverse(self, root, res):

        # Base Case
        if not root: return res

        # Recursive Case
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)

        