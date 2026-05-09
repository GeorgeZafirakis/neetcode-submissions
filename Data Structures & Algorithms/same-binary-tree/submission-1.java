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
    public boolean isSameTree(TreeNode p, TreeNode q) {

        Queue<TreeNode> queueP = new LinkedList<>();
        Queue<TreeNode> queueQ = new LinkedList<>();
        queueP.add(p);
        queueQ.add(q);

        while( !queueQ.isEmpty() && !queueP.isEmpty() ) {

            for ( int i = 0; i < queueP.size(); i++ ) {

                TreeNode nodeP = queueP.poll();
                TreeNode nodeQ = queueQ.poll();

                if (nodeP == null && nodeQ == null) continue;
                if (nodeP == null || nodeQ == null || nodeP.val != nodeQ.val) return false;
                
                queueP.add(nodeP.left);
                queueQ.add(nodeQ.left);
                queueP.add(nodeP.right);
                queueQ.add(nodeQ.right);

            }
        }
        return true;
    }
}

// class Solution {
//     public boolean isSameTree(TreeNode p, TreeNode q) {

//         if (p == null && q == null) return true;
//         if (p == null && q != null) return false;
//         if (p != null && q == null) return false;
//         if (p.val != q.val) return false;

//         return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
//     }
// }
