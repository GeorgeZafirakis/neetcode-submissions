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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        if ( root == null ) return null;
        TreeNode curr = root;

        while ( curr != null ) {

            if ( curr.val > p.val && curr.val > q.val) {
                curr = curr.left;
            } else if ( curr.val < p.val && curr.val < q.val) {
                curr = curr.right;
            } else {
                return curr;
            }
        }
        return null;
    }
}



// class Solution {
//     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

//         if ( root == null ) return null;

//         if ( root.val > p.val && root.val > q.val) {
//             return lowestCommonAncestor(root.left, p, q);
//         }

//         if ( root.val < p.val && root.val < q.val) {
//             return lowestCommonAncestor(root.right, p, q);
//         }

//         return root; 
 
//     }
// }
