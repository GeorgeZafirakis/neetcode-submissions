# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        myList = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            myList.append(node.val)
            traverse(node.right)
            return

        traverse(root)

        for i in range(len(myList) - 1):
            if myList[i+1] <= myList[i]:
                return False

        return True

