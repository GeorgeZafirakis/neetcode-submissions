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
    public ListNode reverseList(ListNode head) {

        if ( head == null ) return head;

        ListNode prev = null;
        ListNode curr = head;
        
        while ( curr != null ) {

            // Add a pointer to next node of the list (in regards to curr node)
            ListNode nextNode = curr.next;

            // Reverse pointer from curr to point to previous position
            curr.next = prev;

            // Move prev pointer by 1 position
            prev = curr;

            // Move cur by 1 position
            curr = nextNode;
        }
    return prev;
    }
}
