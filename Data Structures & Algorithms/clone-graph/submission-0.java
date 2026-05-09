/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;

        Map<Node, Node> table = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();

        Node clonedNode = new Node(node.val);
        table.put(node, clonedNode);
        queue.add(node);

        // BFS Traversal
        while (!queue.isEmpty()) {
            Node currNode = queue.poll();
            Node clonedCurrNode = table.get(currNode); // Get cloned version of current node

            // Clone neighbors
            for (Node neighbor : currNode.neighbors) {
                if (!table.containsKey(neighbor)) {
                    Node clonedNeighbor = new Node(neighbor.val);
                    table.put(neighbor, clonedNeighbor);
                    queue.add(neighbor);
                }
                // Add cloned neighbor to the cloned node's neighbor list
                Node clonedNeighbor = table.get(neighbor);
                clonedCurrNode.neighbors.add(clonedNeighbor);
            }
        }
        return clonedNode;
    }
}


// class Solution {

//     public Node cloneGraph(Node node) {

//        if ( node == null ) return null;

//        Map<Node,Node> map = new HashMap<>();

//        return clone(node, map);
//     }

//     private Node clone(Node node, Map<Node,Node> table) {

//         if (table.containsKey(node)) {
//             // Return the copied node from the table
//             return table.get(node);
//         }

//         Node clonedNode = new Node(node.val);
//         // Add copied cloned node to the table
//         table.put(node,clonedNode);

//         for ( Node n : node.neighbors) {
//             clonedNode.neighbors.add(clone(n, table));
//         }

//         return clonedNode;
//     }
// }