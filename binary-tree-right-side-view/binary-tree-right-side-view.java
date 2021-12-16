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
    public List<Integer> rightSideView(TreeNode root) 
    {
        // No tree exists, return empty list
        List<Integer> answer = new ArrayList<>();
        if (root == null) 
            return answer;
        
        // Setup for BFS and track nodes on each level
        Deque<TreeNode> queue = new LinkedList<>();
        queue.addLast(root);
        int currentLevel = 1, nextLevel = 0;
        
        // BFS
        while (!queue.isEmpty())
        {
            // Pop the node
            TreeNode node = queue.removeFirst();
            currentLevel -= 1;
            
            // Check left
            if (node.left != null) 
            {
                queue.addLast(node.left);
                nextLevel += 1;
            }
            // Check right
            if (node.right != null)
            {
                queue.addLast(node.right);
                nextLevel += 1;
            }
            
            // End of current level, add to right-side list
            // Update level counts
            if (currentLevel == 0)
            {
                answer.add(node.val);
                currentLevel = nextLevel;
                nextLevel = 0;
            }
        }
        
        return answer;
    }
}