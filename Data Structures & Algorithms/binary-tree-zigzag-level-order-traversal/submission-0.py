# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            deck = []
            for i in range(len(q)):
                node = q.popleft()
                deck.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(deck)

        zigRes = []
        for i in range(len(res)):
            if i % 2 == 0:
                zigRes.append(res[i])
            else:
                zigRes.append(res[i][::-1])
        return zigRes

