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

    // Global variable;
    int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {

        if ( root == null ) return 0;
        
        int diameter = maxHeight(root.left) + maxHeight(root.right);
        if ( diameter > maxDiameter) maxDiameter = diameter;

        // Traverse tree
        diameterOfBinaryTree(root.left);
        diameterOfBinaryTree(root.right);

        return maxDiameter;
    }

    private int maxHeight(TreeNode root) {

        // Base Case
        if ( root == null ) return 0;
        // Recursive Case
        return 1 + Math.max(maxHeight(root.left) , maxHeight(root.right));
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
