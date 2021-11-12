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
    public int minDiffInBST(TreeNode root) 
    {
        if (root == null) // No tree exists
            return 0;
        
        // Inorder traversal to get elements in sorted order
        List<Integer> list = new ArrayList<>();
        inorder(root, list);
        
        // Look for smallest gap between sorted elements
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < list.size()-1; i++)
            answer = Math.min(answer, list.get(i+1) - list.get(i));
        return answer;
    }
    
    public void inorder(TreeNode root, List<Integer> list)
    {
        if (root == null) return;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}