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
    public List<TreeNode> generateTrees(int n) 
    {
        return generate(1, n); //Recursively generate trees
    }
    
    public List<TreeNode> generate(int start, int end)
    {
        // Create list for trees
        List<TreeNode> answer = new ArrayList<TreeNode>();
        
        // Base Case, add final node or add no node
        if (start >= end)
        {
            TreeNode node = new TreeNode(start);
            if (start == end) 
                answer.add(node);
            else 
                answer.add(null);
            return answer;
        }
        
        // Partition start and end to generate nodes inbetween for left & right
        for (int mid = start; mid <= end; mid++)
        {
            // Lists for left/right subtrees
            List<TreeNode> left = generate(start, mid-1);
            List<TreeNode> right = generate(mid+1, end);
            
            // Generate new trees
            for (TreeNode L : left)
                for (TreeNode R : right)
                {
                    TreeNode node = new TreeNode(mid);
                    node.left = L;
                    node.right = R;
                    answer.add(node);
                }
        }
        
        return answer;
    }
}