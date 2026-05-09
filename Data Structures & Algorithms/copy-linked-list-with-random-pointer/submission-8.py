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
        
        if not head:
            return None

        myMap = {}
        curr  = head

        # First Pass -> Store Node values only
        while curr:
            myMap[curr] = Node(curr.val)
            curr = curr.next

        # Second Pass -> Fill Node pointers
        curr = head
        while curr:

            myMap[curr].next   = myMap.get(curr.next)
            myMap[curr].random = myMap.get(curr.random)
            curr = curr.next 

        return myMap[head]