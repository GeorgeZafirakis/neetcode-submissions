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

       Queue<TreeNode> queue   = new LinkedList<>();
       List<List<Integer>> res = new LinkedList<>();

       queue.add(root);
       while (!queue.isEmpty()) {

            List<Integer> level = new LinkedList<>();
            int queueSize = queue.size();

            for ( int i = 0; i < queueSize; i++) {
                
                TreeNode node = queue.poll();
                if ( node != null) {
                    queue.add(node.left);
                    queue.add(node.right);
                    level.add(node.val);
                }

            }
            if ( level.size() > 0 ) res.add(level);
       }
       return res;
    }
}
