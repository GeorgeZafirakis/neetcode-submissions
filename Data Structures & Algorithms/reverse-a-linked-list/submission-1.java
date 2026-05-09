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

        ListNode curr = head;
        ListNode prev = null;

        while ( curr != null ) {

            // Keep a pointer to next node of the linkedlist
            ListNode next = curr.next;

            // Use current and prev node to reverse pointer
            curr.next = prev;

            // Move prev 1 position forward
            prev = curr;

            // Move curr 1 position;
            curr = next;
        }
        return prev;
    }
}

// class Solution {
//     public ListNode reverseList(ListNode head) {

//         if ( head == null ) return head;

//         List<Integer> list = new ArrayList<>();
//         ListNode curr = head;

//         while ( curr != null ) {
//             list.add(curr.val);
//             curr = curr.next;
//         }

//         // Reverse list
//         Collections.reverse(list);

//         ListNode newHead = new ListNode(list.get(0));
//         curr = newHead;

//         for ( int i = 1; i < list.size(); i++ ) {
//             curr.next = new ListNode(list.get(i));
//             curr = curr.next;
//         }
//         return newHead;
//     }
// }

// class Solution {
//     public ListNode reverseList(ListNode head) {

//         ListNode curr = head;
//         ListNode prev = null;

//         while ( curr != null ) {

//             // Create next node to help traverse linkedlist by 1 step
//             ListNode next = curr.next;
//             // Change the direction of the pointer ( from "prev -> next" to "next -> prev" )
//             curr.next = prev;
//             // Move prev node 1 step forward
//             prev = curr; 
//             // Move curr node 1 step forward
//             curr = next;
//         }
//         return prev;
//     }
// }
