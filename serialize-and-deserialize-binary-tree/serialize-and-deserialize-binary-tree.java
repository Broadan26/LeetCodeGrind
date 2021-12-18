/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    /* Encodes a tree to a single string. */
    public String serialize(TreeNode root) 
    {
        StringBuilder serial = new StringBuilder();
        
        buildString(root, serial);
        
        return serial.toString();
    }
    
    /* Perform preorder traversal to serialize the tree*/
    private void buildString(TreeNode root, StringBuilder serial)
    {
        if (root == null)
        {
            serial.append("#").append(",");
            return;
        }
        
        serial.append(root.val).append(",");
        buildString(root.left, serial);
        buildString(root.right, serial);
    }

    /* Decodes encoded data to tree. */
    public TreeNode deserialize(String data) 
    {
        Deque<String> tree = new LinkedList<>();
        
        tree.addAll(Arrays.asList(data.split(",")));
        
        return buildTree(tree);
    }
    
    /* Rebuild the tree using preorder flattening properties */
    private TreeNode buildTree(Deque<String> tree)
    {
        // Pop the value
        String val = tree.removeFirst();
        
        // Value is null
        if (val == null || val.equals("#")) 
            return null;
        
        // Value exists
        TreeNode root = new TreeNode(Integer.valueOf(val));
        root.left = buildTree(tree);
        root.right = buildTree(tree);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));