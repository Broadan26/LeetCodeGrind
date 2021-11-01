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
    public int rangeSumBST(TreeNode root, int low, int high) 
    {
        int rangeSum = 0;
        if (root == null) // No tree exists
            return rangeSum;
        
        // DFS for other values in range
        rangeSum += rangeSumBST(root.left, low, high);
        rangeSum += rangeSumBST(root.right, low, high);
        
        if (root.val >= low && root.val <= high)
            return rangeSum + root.val;
        else
            return rangeSum;
    }
}