/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {

        if ( head == null ) return head;

        Map<Node,Node> map = new HashMap<>();
        
        // Add the null node to map to avoid edge cases
        map.put(null, null);
        
        // Made a copy of all nodes of linkedlist without their pointers;
        Node curr = head;
        while( curr != null ) {
            map.put(curr, new Node(curr.val));
            // Move to next node
            curr = curr.next;
        }

        // Reset pointer to start of linkedlist
        curr = head;
        while( curr != null ) {
            Node copy   = map.get(curr);
            copy.next   = map.get(curr.next);
            copy.random = map.get(curr.random); 
            // Move to next node
            curr = curr.next;
        }

        return map.get(head); 
    }
}
