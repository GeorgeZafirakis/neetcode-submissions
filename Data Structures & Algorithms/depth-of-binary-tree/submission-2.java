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
    public int maxDepth(TreeNode root) {

        if ( root == null ) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int level = 0;

        while( !queue.isEmpty() ) {

            int size = queue.size();
            for (int i = 0; i < size; i++) {

                // Get TreeNode stored in the queue
                TreeNode curr = queue.poll();

                // Add childeren of current node to queue
                if (curr.left  != null) queue.add(curr.left);
                if (curr.right != null) queue.add(curr.right);
            }
            level++;
        }
        return level;
    }
}

// class Solution {
//     public int maxDepth(TreeNode root) {

//         if ( root == null ) return 0;

//         return 1 + Math.max( maxDepth(root.left) , maxDepth(root.right) );
        
//     }
// }
