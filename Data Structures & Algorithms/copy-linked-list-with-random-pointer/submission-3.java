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
        Node cur = head;
        
        while ( cur != null ) {
            // Make a new cell and copy the value of the current cell
            Node copy = new Node(cur.val);
            map.put(cur, copy);
            // Traverse linked list
            cur = cur.next;
        }
        
        // Reset cur pointer
        cur = head;
        while ( cur != null ) {
            Node copy   = map.get(cur);
            copy.next   = map.get(cur.next);
            copy.random = map.get(cur.random);
            // Traverse linkedList
            cur = cur.next;
        }
        return map.get(head);
    }
}
