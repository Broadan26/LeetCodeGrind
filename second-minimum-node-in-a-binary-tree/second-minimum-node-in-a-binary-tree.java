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
    public int findSecondMinimumValue(TreeNode root) 
    {
        // No tree exists
        if (root == null) return -1;
        
        // DFS the tree and hash each value for later
        HashSet<Integer> treeSet = new HashSet<Integer>();
        DFS(root, treeSet);
        
        // Tree is all repeat elements
        if (treeSet.size() < 2) return -1;
        
        // Find the second lowest value in the hashset
        int min = Integer.MAX_VALUE, sMin = Integer.MAX_VALUE;
        for (int num: treeSet)
        {
            if (num < min)
            {
                sMin = min;
                min = num;
            }
            else if (num < sMin)
                sMin = num;
        }
        
        return sMin;
    }
    
    private void DFS(TreeNode root, HashSet<Integer> treeSet)
    {
        if (root != null)
        {
            treeSet.add(root.val);
            DFS(root.left, treeSet);
            DFS(root.right, treeSet);
        }
    }
}