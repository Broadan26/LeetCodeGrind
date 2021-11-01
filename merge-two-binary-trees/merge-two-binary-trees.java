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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) 
    {
        if (root1 == null && root2 == null) // Both trees are empty
            return null;
        if (root1 == null) // Tree 1 is empty
            return root2;
        else if (root2 == null) // Tree 2 is empty
            return root1;
        
        root1.val += root2.val; // Merge values
        root1.left = mergeTrees(root1.left, root2.left);
        root1.right = mergeTrees(root1.right, root2.right);
        return root1;
    }
}