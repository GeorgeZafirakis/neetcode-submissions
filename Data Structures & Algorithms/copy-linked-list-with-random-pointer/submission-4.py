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
        cur = head

        while cur:
            myMap[cur] = Node(cur.val)
            cur = cur.next
        cur = head

        while cur:
            cNode        = myMap[cur]
            cNode.next   = myMap[cur.next]
            cNode.random = myMap[cur.random]
            cur = cur.next
        
        return myMap[head]

        
        