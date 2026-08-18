# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Find length
        length = 0
        cur    = head
        
        while cur:
            length += 1
            cur = cur.next

        # Find node BEFORE the one we want to remove
        cur = dummy
        for _ in range(length - n):
            cur = cur.next

        # Remove node
        cur.next = cur.next.next

        return dummy.next