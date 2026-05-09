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

    List<Integer> heightList = new ArrayList<>();

    public int diameterOfBinaryTree(TreeNode root) {

        if ( root == null ) return 0;

        int leftHeight  = maxHeight(root.left);
        int rightHeight = maxHeight(root.right);
        int diameter    = leftHeight + rightHeight;
        heightList.add(diameter);

        diameterOfBinaryTree(root.left);
        diameterOfBinaryTree(root.right);

        return Collections.max(heightList);


    }

    private int maxHeight(TreeNode root) {

        if ( root == null ) return 0;

        return 1 + Math.max(maxHeight(root.left), maxHeight(root.right));

    }

}

// class Solution {

//     // Global variables
//     int maxDiameter = 0;

//     public int diameterOfBinaryTree(TreeNode root) {
//         maxHeight(root);
//         return maxDiameter; 
//     }

//     private int maxHeight(TreeNode root) {

//         if ( root == null) return 0;

//         int leftHeight  = maxHeight(root.left);
//         int rightHeight = maxHeight(root.right);

//         maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

//         return 1 + Math.max(leftHeight, rightHeight);
//     }
// }




// class Solution {

//     // Global variables
//     int diameter = 0, maxDiameter = 0;

//     public int diameterOfBinaryTree(TreeNode root) {

//         // Base Case
//         if ( root == null ) return 0;

//         int maxLeftDepth  = maxHeight(root.left);
//         int maxRightDepth = maxHeight(root.right);
//         diameter = maxRightDepth + maxLeftDepth;
//         if ( diameter > maxDiameter) maxDiameter = diameter;

//         diameter = Math.max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right));

//         if ( diameter > maxDiameter) maxDiameter = diameter;

//         return maxDiameter;
        
//     }

//     public int maxHeight(TreeNode root) {

//         if ( root == null ) return 0;

//         return 1 + Math.max(maxHeight(root.left) , maxHeight(root.right));
//     }
// }
