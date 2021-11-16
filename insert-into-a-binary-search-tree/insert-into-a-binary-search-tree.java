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
    public TreeNode insertIntoBST(TreeNode root, int val) 
    {
        if (root == null) // No tree exists
            return new TreeNode(val);
        
        DFSInsert(root, val); // Perform insertion
        return root;
    }
    
    public void DFSInsert(TreeNode node, int val)
    {
        if (node.val > val && node.left == null)
            node.left = new TreeNode(val);
        else if (node.val > val)
            DFSInsert(node.left, val);
        else if (node.val < val && node.right == null)
            node.right = new TreeNode(val);
        else
            DFSInsert(node.right, val);
    }
}