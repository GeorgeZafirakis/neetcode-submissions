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
    public int maxDepth(TreeNode root) {
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        stack.push(new Pair<>(root, 1));
        int res = 0;

        while (!stack.isEmpty()) {
            Pair<TreeNode, Integer> current = stack.pop();
            TreeNode node = current.getKey();
            int depth = current.getValue();

            if (node != null) {
                res = Math.max(res, depth);
                stack.push(new Pair<>(node.right, depth + 1));
                stack.push(new Pair<>(node.left, depth + 1));
            }
        }
        return res;
    }
}



// class Solution {
//     public int maxDepth(TreeNode root) {

//         if ( root == null ) return 0;

//         return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
//     }
// }




// class Solution {
//     public int maxDepth(TreeNode root) {

//         if ( root == null ) return 0;

//         Queue<TreeNode> queue = new LinkedList<>();
//         queue.add(root);
//         int level = 0;

//         while( !queue.isEmpty() ) {

//             int size = queue.size();
//             for (int i = 0; i < size; i++) {

//                 // Get TreeNode stored in the queue
//                 TreeNode curr = queue.poll();

//                 // Add childeren of current node to queue
//                 if (curr.left  != null) queue.add(curr.left);
//                 if (curr.right != null) queue.add(curr.right);
//             }
//             level++;
//         }
//         return level;
//     }
// }



// class Solution {
//     public int maxDepth(TreeNode root) {

//         if ( root == null ) return 0;

//         return 1 + Math.max( maxDepth(root.left) , maxDepth(root.right) );
        
//     }
// }
