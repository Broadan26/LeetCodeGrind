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
    public boolean isUnivalTree(TreeNode root) 
    {
        if (root == null) // No tree exists
            return true;
        
        int uniValue = root.val; //Every value should be root val
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        while (queue.size() > 0)
        {
            TreeNode node = queue.remove();
            
            if (node.left != null)
                queue.add(node.left);
            if (node.right != null)
                queue.add(node.right);
            
            if (node.val != uniValue) // Not all the same
                return false;
        }
        return true;
    }
}