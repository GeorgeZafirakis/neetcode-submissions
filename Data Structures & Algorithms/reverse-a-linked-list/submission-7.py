# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur  = head

        while cur:

            # set nxt pointer 1 step ahead of cur pointer
            nxt = cur.next
            # reverse pointer of cur node
            cur.next = prev
            # move prev pointer by one step
            prev = cur
            # set cur to next  
            cur = nxt

        return prev