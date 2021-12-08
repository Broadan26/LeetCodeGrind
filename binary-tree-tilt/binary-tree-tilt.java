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
    public int findTilt(TreeNode root) 
    {
        if (root == null) return 0;
        
        // Calculate the tilt of the current node
        int localTilt = 0;
        localTilt = Math.abs(sumDFS(root.left) - sumDFS(root.right));
        
        // Calculate the sum of the tilts of all nodes
        return localTilt + findTilt(root.left) + findTilt(root.right);
    }
    
    // Calculates the sum of any given subtree
    private int sumDFS(TreeNode root)
    {
        if (root == null) return 0;
        return root.val + sumDFS(root.left) + sumDFS(root.right);
    }
}