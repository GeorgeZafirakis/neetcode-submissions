/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        if ( l1 == null && l2 == null ) return null;
        if ( l1 == null ) return l2;
        if ( l2 == null ) return l1;

        // Create a dummy node to return to the start of the linkedlist
        ListNode dummy = new ListNode(-1);
        ListNode curr  = dummy;

        int carry = 0;
        int res   = 0;
        while ( l1 != null || l2 != null || carry != 0 ) {
            int num1  = (l1 != null) ? l1.val : 0;
            int num2  = (l2 != null) ? l2.val : 0;
            int sum   = num1 + num2 + carry;
            carry     = sum / 10;
            res       = sum % 10;
            // Create a new node thatcontains the result
            ListNode node = new ListNode(res);
            // Connect previous and current node in the new linkedlist
            curr.next = node;
            // Move curr node by 1 position
            curr = curr.next;
            // Traverse lists 1 and 2 by one position
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        return dummy.next;
        
    }
}
