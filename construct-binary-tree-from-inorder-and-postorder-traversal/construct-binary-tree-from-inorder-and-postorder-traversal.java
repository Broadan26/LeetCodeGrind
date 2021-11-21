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
    // Inorder: Left->Root->Right
    // PostOrder: Left->Right->Root
    
    public TreeNode buildTree(int[] inorder, int[] postorder) 
    {
        // Nothing more can be done
        if (inorder == null || postorder == null || inorder.length != postorder.length)
            return null;
        
        // Map inorder set of nodes
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < inorder.length; i++)
                map.put(inorder[i], i);
        
        //Recursively build the tree
        return buildTree(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1, map);
    }
    
    private TreeNode buildTree(int[] inorder, int inStart, int inEnd, int[] postorder, int pStart, int pEnd, HashMap<Integer, Integer> map)
    {
        if (pStart > pEnd || inStart > inEnd) // Nothing to do
            return null;
        
        TreeNode root = new TreeNode(postorder[pEnd]); // Build subtree root
        int r = map.get(postorder[pEnd]); // Find root location in inorder
        
        TreeNode left = buildTree(inorder, inStart, r-1, postorder, pStart, pStart+r-inStart-1, map); // Build left subtree
        TreeNode right = buildTree(inorder, r+1, inEnd, postorder, pStart+r-inStart, pEnd-1, map); // Build right subtree
        
        root.left = left; // Add subtrees to root
        root.right = right;
        
        return root;
    }
}