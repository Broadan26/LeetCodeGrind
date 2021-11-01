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
    public List<Integer> inorderTraversal(TreeNode root) 
    {
        List<Integer> nodeList = new ArrayList<Integer>();
        if (root == null)
            return nodeList;
        return DFS(root, nodeList);
    }
    
    public List<Integer> DFS(TreeNode root, List<Integer> nodeList)
    {
        if (root == null)
            return nodeList;
        DFS(root.left, nodeList);
        nodeList.add(root.val);
        DFS(root.right, nodeList);
        return nodeList;
    }
}