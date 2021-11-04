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
    public int sumOfLeftLeaves(TreeNode root) 
    {
        if (root == null) // No tree exists
            return 0;
        
        return DFS(root, false);
    }
    
    public int DFS(TreeNode root, boolean isLeft)
    {
        if (root == null) //No node exists
            return 0;
        
        if (root.left == null && root.right == null && isLeft)
            return root.val;
        int sum = DFS(root.left, true);
        sum += DFS(root.right, false);
        return sum;
    }
}