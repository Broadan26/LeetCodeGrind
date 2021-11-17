/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution 
{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) 
    {
        if (root.val > p.val && root.val > q.val) // Traverse left
            return lowestCommonAncestor(root.left, p, q);
        else if (root.val < p.val && root.val < q.val) // Traverse right
            return lowestCommonAncestor(root.right, p, q);
        else // Found lowest common ancestor
            return root;
    }
}