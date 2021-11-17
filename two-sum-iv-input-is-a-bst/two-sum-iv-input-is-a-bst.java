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
class Solution 
{
    public boolean findTarget(TreeNode root, int k) 
    {
        if (root == null) return false; // No tree exists
        
        HashSet<Integer> set = new HashSet<Integer>();
        Deque<TreeNode> queue = new LinkedList<TreeNode>();
        queue.addLast(root);
        
        while (queue.size() > 0)
        {
            // BFS operations
            TreeNode node = queue.removeFirst();
            if (node.left != null) queue.addLast(node.left);
            if (node.right != null) queue.addLast(node.right);
            
            // Hash potential matches as a set
            if (set.contains(node.val))
                return true;
            else
                set.add(k-node.val);
        }
        return false;
    }
}