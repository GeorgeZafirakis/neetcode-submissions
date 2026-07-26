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

            # Set pointer to next node of linked list
            nxt = cur.next
            # Invert pointer position
            cur.next = prev
            # Move previous pointer by 1 position
            prev = cur
            # Move cur by 1 position
            cur = nxt

        return prev