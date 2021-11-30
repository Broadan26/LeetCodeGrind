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
    public int getMinimumDifference(TreeNode root) 
    {
        if (root == null) return Integer.MAX_VALUE;
        
        int minDiff = Integer.MAX_VALUE; // Track the minimum value
        List<Integer> search = new ArrayList<>(); // Create list of nodes
        
        return traverse(root, minDiff, search); // Inorder traversal
    }
    
    /* Inorder Traversal of the BST */
    private int traverse(TreeNode root, int minDiff, List<Integer> search)
    {
        // Add left subtree
        if (root.left != null)
            minDiff = traverse(root.left, minDiff, search);
        
        // Add root
        search.add(root.val);
        
        // Check for a minimum difference
        if (search.size() > 1)
        {
            int currDiff = search.get(search.size()-1) - search.get(search.size()-2);
            if (currDiff < minDiff) 
                minDiff = currDiff;
        }
        
        // Add right subtree
        if (root.right != null)
            minDiff = traverse(root.right, minDiff, search);
        
        return minDiff;
    }
}