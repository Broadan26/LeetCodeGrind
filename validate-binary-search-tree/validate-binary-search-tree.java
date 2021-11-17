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
    public boolean isValidBST(TreeNode root) 
    {
        return validateBST(root, null, null);
    }
    
    private boolean validateBST(TreeNode root, TreeNode min, TreeNode max)
    {
        // No node, is valid
        if (root == null) return true;
        
        // Current node breaks BST bounds
        if (min != null && root.val <= min.val || max != null && root.val >= max.val)
            return false;
        
        // Recursively validate the tree via DFS
        return validateBST(root.left, min, root) && validateBST(root.right, root, max);
    }
}