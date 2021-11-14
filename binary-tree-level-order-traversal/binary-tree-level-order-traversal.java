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
    public List<List<Integer>> levelOrder(TreeNode root) 
    {
        List<List<Integer>> nodes = new ArrayList<>();
        if (root == null) // No tree exists
            return nodes;
        
        // Setup BFS
        List<Integer> level = new ArrayList<Integer>();
        Deque<TreeNode> queue = new LinkedList<TreeNode>();
        queue.addLast(root);
        int currentLevel = 1, nextLevel = 0;
        
        while (!queue.isEmpty()) // BFS
        {
            TreeNode node = queue.removeFirst();
            level.add(node.val);
            currentLevel -= 1;
            
            if (node.left != null) // Check left
            {
                queue.addLast(node.left);
                nextLevel += 1;
            }
            if (node.right != null) // Check right
            {
                queue.addLast(node.right);
                nextLevel += 1;
            }
            
            if (currentLevel == 0) // Check if current level ended
            {
                currentLevel = nextLevel;
                nextLevel = 0;
                nodes.add(level);
                level = new ArrayList<Integer>();
            }
        }
        
        return nodes;
    }
}