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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if ( list1 == null ) return list2;
        if ( list2 == null ) return list1;

        ListNode curr = new ListNode(-1);
        ListNode res  = curr;

        while( list1 != null && list2 != null ) {           
            
            if ( list1.val <= list2.val ) {
                // Set curr pointer to list1
                curr.next = list1;
                // Traverse list1 by 1 node
                list1 = list1.next;
                // Move curr by 1 position
                curr = curr.next;
            } else {
                curr.next = list2;
                list2 = list2.next;
                curr  = curr.next;
            }
        }

        if ( list1 == null ) {
            curr.next = list2;
        }

        if ( list2 == null ) {
            curr.next = list1;
        }

        return res.next;
    }
}


// class Solution {
//     public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

//         if ( list1 == null ) return list2;
//         if ( list2 == null ) return list1;

//         if ( list1.val <= list2.val ) {
//             list1.next = mergeTwoLists(list1.next, list2);
//             return list1;
//         } else {
//             list2.next = mergeTwoLists(list1, list2.next);
//             return list2;
//         }

//     }
// }



































// class Solution {
//     public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

//         if ( list1 == null && list2 == null ) return null;
//         if ( list1 == null ) return list2;
//         if ( list2 == null ) return list1;
        
//         ListNode curr = new ListNode(-1000);
//         ListNode head = curr;

//         while ( list1 != null && list2 != null ) {
//             if ( list1.val <= list2.val ) {
//                 curr.next = list1;
//                 list1 = list1.next;
//             } else {
//                 curr.next = list2;
//                 list2 = list2.next;
//             }
//             curr = curr.next;
//         }

//         if ( list1 == null && list2 == null ) {
//             return head.next;
//         } else if ( list1 == null ) {
//             curr.next = list2;
//             return head.next;
//         } else {
//             curr.next = list1;
//             return head.next;
//         }
    
//     }
// }