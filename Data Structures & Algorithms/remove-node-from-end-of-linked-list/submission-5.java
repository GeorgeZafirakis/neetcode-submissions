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
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode dummy = new ListNode (-1, head);
        // Start with the slow pointer one position behind the head
        ListNode left  = dummy;
        ListNode right = head;

        int counter = n;
        while ( n > 0 ) {
            right = right.next;
            n--;
        }

        while ( right != null ) {     
            left  = left.next;
            right = right.next;
        }
        // Skip intermediate node
        left.next = left.next.next;


        return dummy.next;
    }
}
