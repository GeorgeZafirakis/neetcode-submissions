/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    Integer prev = null;  // Store the previous value during in-order traversal

    public boolean isValidBST(TreeNode root) {
        return inOrderTraversal(root);
    }

    private boolean inOrderTraversal(TreeNode node) {
        if (node == null) return true;  // Base case: Empty tree is a BST

        // Left subtree check
        if (!inOrderTraversal(node.left)) return false;

        // Check current node against previous node
        if (prev != null && node.val <= prev) return false;

        prev = node.val;  // Update previous node value

        // Right subtree check
        return inOrderTraversal(node.right);
    }
}


// public class Solution {

//     List<Integer> list = new LinkedList<>();

//     public boolean isValidBST(TreeNode root) {
//        inOrderTraversal(root);

//        if ( list == null ) return true;
//        for ( int i = 0; i < list.size() - 1; i++) {
//         int curr = list.get(i);
//         int next = list.get(i+1);
//         if ( curr >= next ) return false;
//        }
//        return true;
//     }

//     private void inOrderTraversal(TreeNode root) {
//         // Base case
//         if ( root == null ) return;

//         // Recursive case
//         inOrderTraversal(root.left);
//         list.add(root.val);
//         inOrderTraversal(root.right);
//     }
// }


