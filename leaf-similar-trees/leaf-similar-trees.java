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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) 
    {
        if (root1 == null && root2 == null) // No trees
            return true;
        if (root1 == null || root2 == null) // One tree
            return false;
        
        // Lists to compare
        List<Integer> tree1 = new ArrayList<Integer>();
        List<Integer> tree2 = new ArrayList<Integer>();
        
        // DFS both trees
        DFS(root1, tree1);
        DFS(root2, tree2);
        
        // Compare the lists
        if (tree1.size() != tree2.size()) // List lengths differ
            return false;
        for (int i = 0; i < tree1.size(); i++) // Compare each element
        {
            if (tree1.get(i) != tree2.get(i))
                return false;
        }
        return true;
    }
    
    public void DFS(TreeNode root, List<Integer> tree)
    {
        if (root == null) // Node node
            return;
        if (root.left == null && root.right == null) // Leaf Node
        {
            tree.add(root.val);
            return;
        }
        DFS(root.left, tree); // DFS again
        DFS(root.right, tree);
    }
}