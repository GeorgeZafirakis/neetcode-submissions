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
    public void reorderList(ListNode head) {

        if ( head == null ) return;

        List<Integer> list    = new ArrayList<>();
        List<Integer> resList = new ArrayList<>();

        // Traverse list and store node values into arraylist

        ListNode curr = head;
        while( curr != null ) {
            list.add(curr.val);
            curr = curr.next;
        }

        for ( int i = 0; i < list.size() / 2; i++ ) {

            resList.add(list.get(i));
            resList.add(list.get(list.size() - 1 - i));
        }
        // Deal with odd list
        if ( list.size() % 2 == 1 ) resList.add(list.get(list.size() / 2 ));

        curr = head;
        for ( int  i = 1; i < resList.size(); i++ ) {
            ListNode node = new ListNode(resList.get(i));
            curr.next = node;
            curr = curr.next;
        }

    }
}

