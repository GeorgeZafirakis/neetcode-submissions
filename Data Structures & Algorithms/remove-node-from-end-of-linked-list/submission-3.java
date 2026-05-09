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

        ListNode helper = new ListNode(-1, head);
        ListNode left   = helper;
        ListNode right  = head;

        while ( n > 0 ) {
            // Traverse n nodes from linkedlist with right pointer
            right = right.next;
            n--;
        }

        while ( right != null ) {
            // Traverse linkedlist with both left and right pointer
            left  = left.next;
            right = right.next;
        }

        // Skip node of linkedlist
        left.next = left.next.next;

        return helper.next;
    }
}

// class Solution {
//     public ListNode removeNthFromEnd(ListNode head, int n) {

//         ListNode curr = head;
//         int size = 0;

//         while ( curr != null ) {
//             curr = curr.next;
//             size++;
//         }

//         if ( n == size ) return head.next;

//         // Reset curr node
//         curr = head;
//         // Traverse 
//         while ( size - n - 1 > 0 ) {
//             curr = curr.next;
//             size--;
//         }
//         // Skip node
//         curr.next = curr.next.next;

//         return head;

//     }
// }


