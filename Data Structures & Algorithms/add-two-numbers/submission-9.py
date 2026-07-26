# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy     = ListNode()
        cur       = dummy
        prevCarry = 0

        while l1 or l2:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            digit = (l1_val + l2_val + prevCarry) % 10
            carry = (l1_val + l2_val + prevCarry) // 10
            prevCarry = carry

            newNode  = ListNode(digit)
            cur.next = newNode

            cur   = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry == 1:
            newNode  = ListNode(carry)
            cur.next = newNode

        return dummy.next

