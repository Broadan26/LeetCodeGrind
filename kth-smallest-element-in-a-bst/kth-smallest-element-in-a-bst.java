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
    public int kthSmallest(TreeNode root, int k) 
    {
        // No tree, cannot return smallest element
        if (root == null)
            return -1;
        
        // Create an inorder list of integers
        List<Integer> inorder = new ArrayList<>();
        
        // DFS the tree to build inorder list of int
        DFS(root, inorder, k);
        
        // Return answer if k in bounds
        if (k > inorder.size()) 
            return -1;
        return inorder.get(k-1);
    }
    
    private void DFS(TreeNode root, List<Integer> inorder, int k)
    {
        // Subtree does not exist, do nothing
        if (root == null) return;
        
        // Inorder DFS traversal
        DFS(root.left, inorder, k);
        inorder.add(root.val);
        DFS(root.right, inorder, k);
    }
}