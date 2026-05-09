# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        wolf  = dummy
        rabit = head

        for _ in range(n):
            rabit = rabit.next

        while rabit:
            rabit = rabit.next
            wolf  = wolf.next

        wolf.next = wolf.next.next
        return dummy.next 