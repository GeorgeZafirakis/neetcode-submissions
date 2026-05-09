# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return

        # Use fast and slow pointer to find mid of linkedlist
        slow  = head
        fast  = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next  

        # Use slow pointer to reverse second half of linkedlist
        prev = None
        cur  = slow.next
        # Cut first half
        slow.next = None

        while cur:
            nxt      = cur.next 
            cur.next = prev
            prev     = cur
            cur      = nxt

        # Connect first and second part ( interleaving )
        cur  = head
        tail = prev
        while tail:
            nxt       = cur.next
            tmp_tail  = tail.next

            cur.next  = tail
            tail.next = nxt
            
            cur       = nxt
            tail      = tmp_tail

        return












