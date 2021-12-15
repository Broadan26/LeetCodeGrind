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
    public TreeNode sortedArrayToBST(int[] nums) 
    {
        // No tree can be built
        if (nums.length < 1) return null;
        
        // Build the tree using DFS
        TreeNode root = DFS(nums, 0, nums.length-1);
        
        return root;
    }
    
    private TreeNode DFS(int[] nums, int low, int high)
    {
        // Finished this subtree
        if (low > high) return null;
        
        // Find mid (avoid integer overflow)
        int mid = low + (high-low) / 2;
        
        // Create a subtree root
        TreeNode root = new TreeNode(nums[mid]);
        
        // Build the subtree child nodes
        root.left = DFS(nums, low, mid-1);
        root.right = DFS(nums, mid+1, high);
        
        // Return the subtree
        return root;
    }
}