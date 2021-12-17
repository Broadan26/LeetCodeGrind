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
class BSTIterator 
{

    private List<Integer> inorder;
    private int location;
    
    public BSTIterator(TreeNode root) 
    {
        // Flatten the tree to perform iteration
        inorder = new ArrayList<>();
        DFS(root);
        location = -1;
    }
    
    private void DFS(TreeNode root)
    {
        // No subtree exists, return
        if (root == null) return;
        
        // Perform inorder DFS traversal
        DFS(root.left);
        inorder.add(root.val);
        DFS(root.right);
    }
    
    public int next() 
    {
        // If location in tree bounds, return values
        if (location+1 < inorder.size())
        {
            location += 1;
            return inorder.get(location);
        }
        return -1;
    }
    
    public boolean hasNext() 
    {
        // If location in bounds, return true
        if (location+1 < inorder.size())
            return true;
        return false;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */