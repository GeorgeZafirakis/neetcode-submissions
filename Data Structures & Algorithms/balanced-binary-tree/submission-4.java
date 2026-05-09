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
        return getHeight(root) != -1;
    }

    private int getHeight(TreeNode root) {

        if ( root == null ) return 0;

        int left = getHeight(root.left);
        if ( left == -1 ) return -1;

        int right = getHeight(root.right);
        if ( right == -1 ) return -1;

        if ( Math.abs( left - right ) > 1 ) {
            return -1;
        }

        return 1 + Math.max( getHeight(root.left) , getHeight(root.right) ); 

    }
 }

// class Solution {
//     public boolean isBalanced(TreeNode root) {

//         if ( root == null ) return true;

//         int leftHeight  = treeHeight(root.left);
//         int rightHeight = treeHeight(root.right);
//         int diff        = Math.abs( leftHeight - rightHeight );

//         if ( diff > 1 ) return false; 

//         return isBalanced(root.left) && isBalanced(root.right);
        
//     }

//     private int treeHeight(TreeNode root) {

//         if ( root == null ) return 0;

//         return 1 + Math.max( treeHeight(root.left) , treeHeight(root.right) );
//     }

// }
