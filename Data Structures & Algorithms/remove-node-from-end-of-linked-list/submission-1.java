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
        if (head == null) return null;

        ListNode dummy = new ListNode(0); // Dummy node to handle head removal
        dummy.next = head;
        ListNode curr = dummy;
        int size = 0;

        // Find size of linked list
        while (curr.next != null) {
            curr = curr.next;
            size++;
        }

        System.out.println("Linked list size: " + size);

        // If removing the first node
        if (n == size) return head.next;

        // Reset curr to dummy
        curr = dummy;

        // Move curr to node before the one to delete
        for (int i = 0; i < size - n; i++) {
            curr = curr.next;
        }

        // Remove nth node
        curr.next = curr.next.next;

        return dummy.next; // Return updated head
    }
}


// class Solution {
//     public ListNode removeNthFromEnd(ListNode head, int n) {

//         if ( head == null ) return head;

//         ListNode curr = head;

//         while ( curr != null ) {

//             // If n greater than size of linkedlist
//             if ( curr.next == null ) {
//                 return null;
//             }

//             // Traverse linkedlist and reduce n after each traversal
//             curr = curr.next;
//             n--;
//             // Stop traversal as we reached n
//             if ( n - 1 == 0) break;
//         }

//         // Jump to next node of the linkedlist if such node exists
//         if ( curr.next.next != null ) {
//             curr.next = curr.next.next;
//             curr = curr.next;
//         }
//         return head;
//     }
// }
