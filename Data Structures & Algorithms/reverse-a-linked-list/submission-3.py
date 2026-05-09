# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            # A new Node after curr Node
            temp = curr.next
            # Reverse the pointer of curr node to oposite direction
            curr.next = prev
            # Prev node traverses linkedlist by 1 step
            prev = curr
            # Curr node traverses linkedlist by 1 step
            curr = temp


        return prev 
        