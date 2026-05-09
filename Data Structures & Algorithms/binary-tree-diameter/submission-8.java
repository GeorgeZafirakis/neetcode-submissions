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

    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {

        if ( root == null ) return 0;

        int leftHeight  = maxDepth(root.left);
        int rightHeight = maxDepth(root.right);
        int diameter    = leftHeight + rightHeight;
        maxDiameter     = Math.max(maxDiameter, diameter);

        diameterOfBinaryTree(root.left);
        diameterOfBinaryTree(root.right);

        return maxDiameter;

    }

    public int maxDepth(TreeNode root) {
       if ( root == null ) return 0;
       return 1 + Math.max(maxDepth(root.left) , maxDepth(root.right));  
    }

}






























// class Solution {

//     int maxDiameter = 0;

//     public int diameterOfBinaryTree(TreeNode root) {
//         dfs(root);
//         return maxDiameter;
//     }

//     private int dfs(TreeNode root) {

//         if ( root == null ) return 0;

//         int left  = dfs(root.left);
//         int right = dfs(root.right);
//         int diameter = left + right;

//         // Update maxDiameter
//         if ( diameter > maxDiameter) maxDiameter = diameter;

//         // Return height
//         return 1 + Math.max(left, right); 
//     }
      

// }
