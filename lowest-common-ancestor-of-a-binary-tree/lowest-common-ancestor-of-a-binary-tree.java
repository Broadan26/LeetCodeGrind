/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution 
{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) 
    {
        // Tree does not exist
        if (root == null) return root;
        
        // Found an ancestor node (self)
        if (root == p || root == q) return root;
        
        // Recursively DFS the tree to find ancestors
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        // Determine which node to return as the common ancestor
        if (left != null && right != null) return root;
        if (left == null) return right;
        return left;
    }
}