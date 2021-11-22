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
    public TreeNode deleteNode(TreeNode root, int key) 
    {
        // Subtree does not exist
        if (root == null)
            return null;
        
        if (key < root.val) // Go left
            root.left = deleteNode(root.left, key);
        else if (key > root.val) // Go Right
            root.right = deleteNode(root.right, key);
        else // Found node
        {
            if (root.left == null) // No lesser node
                return root.right;
            else // Look for largest node on left side
            {
                TreeNode node = root.left;
                while (node.right != null)
                    node = node.right;
                
                // Replace the current node with found node
                root.val = node.val;
                root.left = deleteNode(root.left, node.val);
            }
        }
        
        return root;
    }
}