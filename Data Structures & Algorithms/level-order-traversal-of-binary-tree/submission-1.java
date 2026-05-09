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
    public List<List<Integer>> levelOrder(TreeNode root) {

        Queue<TreeNode>     queue = new LinkedList<>();
        List<List<Integer>> list = new LinkedList<>();

        if ( root == null ) return list;
        
        // Add root to queue
        queue.add(root);

        while(!queue.isEmpty()) {
            int queueSize = queue.size();
            // For each level of the tree, create a new list to store node values
            List<Integer> l = new LinkedList<>();
            for ( int i = 0; i < queueSize; i++) {
                TreeNode node = queue.poll();
                l.add(node.val);
                if (node.left  != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            list.add(l);
        }
        return list;
    }
}
