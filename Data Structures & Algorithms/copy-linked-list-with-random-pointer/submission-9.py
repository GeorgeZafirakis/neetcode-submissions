"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        myMap = {None : None}

        dummy = head
        cur   = head

        # First Pass
        while cur:

            copyNode     = Node(cur.val)
            myMap[cur]   = copyNode
            cur          = cur.next

        # Second Pass
        cur = dummy
        while cur:

            copyNode        = myMap[cur]
            copyNode.next   = myMap[cur.next]
            copyNode.random = myMap[cur.random]
            cur             = cur.next

        cur = dummy
        return myMap[cur]










        