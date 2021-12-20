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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) 
    {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) return answer;
        
        // Setup for BFS
        Deque<TreeNode> queue = new LinkedList<>();
        queue.addLast(root);
        boolean flag = false;
        
        // BFS
        while (!queue.isEmpty())
        {
            int levelSize = queue.size();
            List<Integer> current = new ArrayList<>();
            
            for (int i = 0; i < levelSize; i++)
            {
                TreeNode node = queue.removeFirst();
                
                if (!flag)
                    current.add(node.val);
                else
                    current.add(0,node.val);
                
                if (node.left != null) queue.addLast(node.left);
                if (node.right != null) queue.addLast(node.right);
            }
            
            flag = !flag;
            answer.add(current);
        }
        
        return answer;
    }
}