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
    public boolean isSameTree(TreeNode p, TreeNode q) 
    {
        if (p == null && q == null) // Both empty edge case
            return true;
        else if (p == null || q == null) // One empty edge case
            return false;
        
        // Setup queues for BFS
        Deque<TreeNode> pQ = new LinkedList<TreeNode>();
        Deque<TreeNode> qQ = new LinkedList<TreeNode>();
        pQ.addLast(p);
        qQ.addLast(q);
        
        while (pQ.size() > 0 && qQ.size() > 0) // BFS
        {
            TreeNode pNode = pQ.removeFirst(); // Poll the nodes
            TreeNode qNode = qQ.removeFirst();
            
            if (pNode == null && qNode == null) // Both empty
                continue;
            
            if (pNode == null || qNode == null) // One is empty
                return false;
            
            if (pNode.val != qNode.val) // Values mismatch
                return false;
            pQ.addLast(pNode.left);
            pQ.addLast(pNode.right);
            qQ.addLast(qNode.left);
            qQ.addLast(qNode.right);
        }
        
        return pQ.size() == qQ.size();
    }
}