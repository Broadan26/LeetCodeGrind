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
    public boolean isSymmetric(TreeNode root) 
    {
        if (root == null) // No tree, is symmetric
            return true;
        
        return DFS(root.left, root.right);
    }
    
    public boolean DFS(TreeNode leftNode, TreeNode rightNode)
    {
        if (leftNode == null && rightNode == null) // Both nodes are null
            return true;
        else if (leftNode == null || rightNode == null) // One node is null
            return false;
        else if (leftNode.val != rightNode.val) // Vals don't match
            return false;
        
        
        // DFS like node structure
        return DFS(leftNode.left, rightNode.right) && DFS(leftNode.right, rightNode.left);
    }
}