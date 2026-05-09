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

    public boolean isBalanced(TreeNode root) {
        if ( dfs(root) == -1 ) return false;
        return true;
    }

    private int dfs(TreeNode root) {

        if ( root == null ) return 0;

        int left  = dfs(root.left);
        if ( left == -1 ) return -1;

        int right = dfs(root.right);
        if ( right == -1 ) return -1;

        if ( Math.abs(left - right) > 1 ) return -1;

        return 1 + Math.max(left , right);
    }
}
































// class Solution {

//     public boolean isBalanced(TreeNode root) {
        
//         if ( dfs(root) == -1 ) return false;
//         return true;

//     }

//     private int dfs(TreeNode root) {

//         if ( root == null ) return 0;

//         int left  = dfs(root.left);
//         int right = dfs(root.right);
//         int dif   = Math.abs(left - right);

//         // Update maxDiameter
//         if ( dif > 1 || left == -1 || right == -1) return -1;

//         // Return height
//         return 1 + Math.max(left, right); 
//     }
// }




// class Solution {
//     public boolean isBalanced(TreeNode root) {

//         if ( root == null ) return true;

//         int left  = maxDepth(root.left);
//         int right = maxDepth(root.right);
//         if ( Math.abs(left - right) > 1 ) return false;

//         return isBalanced(root.left) && isBalanced(root.right);  
//     }

//     public int maxDepth(TreeNode root) {

//         if ( root == null ) return 0;

//         return 1 + Math.max(maxDepth(root.left) , maxDepth(root.right) );
        
//     }
// }
