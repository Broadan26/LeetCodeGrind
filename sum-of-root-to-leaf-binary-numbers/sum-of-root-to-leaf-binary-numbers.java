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
    private int sumRootToLeaf = 0;
    
    public int sumRootToLeaf(TreeNode root) 
    {
        // No tree exists
        if (root == null) return 0;
        
        // DFS down the tree keeping track of values in each node
        DFS(root, 0);
        
        return sumRootToLeaf;
    }
    
    private void DFS(TreeNode root, int sum)
    {
        // Node doesnt exist, backtrack
        if (root == null) return;
        
        // Shift bits over 1, add node value as new last bit
        sum = (sum << 1) | root.val;
        
        // If node is a leaf node, add it to running sum
        if (root.left == null && root.right == null)
        {
            sumRootToLeaf += sum;
            return;
        }

        // DFS the other nodes looking for a leaf
        DFS(root.left, sum);
        DFS(root.right, sum);
    }
}