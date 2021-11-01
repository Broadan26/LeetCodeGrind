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
    public int minDepth(TreeNode root) 
    {
        int depth = 1;
        if (root == null)
            return 0;
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        int currentLevel = 1;
        int nextLevel = 0;
        while (currentLevel > 0)
        {
            TreeNode node = queue.remove();
            currentLevel--;
            
            // Found highest leaf node
            if (node.left == null && node.right == null)
                return depth;
            
            if (node.left != null)
            {
                queue.add(node.left);
                nextLevel++;
            }
            if (node.right != null)
            {
                queue.add(node.right);
                nextLevel++;
            }
            
            if (currentLevel == 0)
            {
                currentLevel = nextLevel;
                nextLevel = 0;
                depth++;
            }
        }
        
        return depth;
    }
}