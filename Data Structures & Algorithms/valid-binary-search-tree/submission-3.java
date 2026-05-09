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

public class Solution {

    List<Integer> list = new LinkedList<>();

    public boolean isValidBST(TreeNode root) {
       inOrderTraversal(root);

       if ( list == null ) return true;
       for ( int i = 0; i < list.size() - 1; i++) {
        int curr = list.get(i);
        int next = list.get(i+1);
        if ( curr >= next ) return false;
       }
       return true;
    }

    private void inOrderTraversal(TreeNode root) {
        // Base case
        if ( root == null ) return;

        // Recursive case
        inOrderTraversal(root.left);
        list.add(root.val);
        inOrderTraversal(root.right);
    }
}


