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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) 
    {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) 
            return answer;
        
        DFS(root, targetSum, answer, new ArrayList<>());
        
        return answer;
    }
    
    private void DFS(TreeNode node, int target, List<List<Integer>> answer, List<Integer> current)
    {
        // No node exists
        if (node == null) return;
        
        // Target value reached & is a leaf node
        else if (target - node.val == 0 && node.left == null && node.right == null)
        {
            current.add(node.val);
            answer.add(new ArrayList<>(current));
            current.remove(current.size()-1);
            return;
        }
        
        // Perform DFS and keep track of values seen
        current.add(node.val);
        DFS(node.left, target - node.val, answer, current);
        DFS(node.right, target - node.val, answer, current);
        current.remove(current.size()-1);
    }
}