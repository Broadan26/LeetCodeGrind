/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution 
{
    public Node connect(Node root) 
    {
        if (root == null) // No tree
            return root;
        
        // Create queue for BFS
        Deque<Node> queue = new LinkedList<Node>();
        queue.addLast(root);
        int currentLevel = 1, nextLevel = 0;
        while (queue.size() > 0) // BFS
        {
            Node node = queue.removeFirst();
            currentLevel--;
            
            if (node.left != null) // Check left
            {
                queue.addLast(node.left);
                nextLevel++;
            }
            if (node.right != null) // Check right
            {
                queue.addLast(node.right);
                nextLevel++;
            }
            
            if (currentLevel == 0) // Check next
            {
                currentLevel = nextLevel;
                nextLevel = 0;
            }
            else // Add next
                node.next = queue.peekFirst();
        }
        return root;
    }
}