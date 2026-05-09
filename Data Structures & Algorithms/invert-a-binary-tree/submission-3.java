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
    public TreeNode invertTree(TreeNode root) {

        Queue<TreeNode> queue = new LinkedList<>();

        if ( root == null ) return root;
        queue.add(root);

        while ( ! queue.isEmpty() ) {

            TreeNode node = queue.poll();
            
            // Helper Node
            TreeNode temp  = node.left;

            // Reverse left and right child
            node.left  = node.right;
            node.right = temp;

            // Add children of new nodes to queue
            if ( node.left  != null ) queue.add(node.left);
            if ( node.right != null ) queue.add(node.right);

            
        }
        return root;
    }
 }

//  class Solution {
//     public TreeNode invertTree(TreeNode root) {

//         if ( root == null) return root;

//         TreeNode node = new TreeNode(root.val);
//         node.right = invertTree(root.left);
//         node.left  = invertTree(root.right);

//         return node;        
//     }
//  }








































// class Solution {
//     public TreeNode invertTree(TreeNode root) {
        
//         if ( root == null ) return root;

//         Queue<TreeNode> queue = new LinkedList<>();
//         queue.add(root);

//         while (!queue.isEmpty()) {

//             TreeNode curr = queue.poll();

//             // Swap left and right
//             TreeNode temp = curr.left;
//             curr.left     = curr.right;
//             curr.right    = temp;

//             if ( curr.left  != null ) queue.add(curr.left);
//             if ( curr.right != null ) queue.add(curr.right);
//         }

//         return root; 

//     }
// }









// class Solution {
//     public TreeNode invertTree(TreeNode root) {
        
//         if ( root == null ) return root;

//         TreeNode temp = root.left;
//         root.left     = invertTree(root.right);
//         root.right    = invertTree(temp);

//         return root; 

//     }
// }



