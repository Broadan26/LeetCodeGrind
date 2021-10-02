import java.util.ArrayList;

public class Solution 
{
	public void recoverTree(TreeNode root)
	{
		ArrayList<TreeNode> node_list = new ArrayList<TreeNode>();
		node_list = inorderDFS(root, node_list);
		
		int length = node_list.size();
		TreeNode first = null;
		TreeNode second = null;
		for(int i = 1; i < length; i++)
		{
			if (node_list.get(i).val < node_list.get(i-1).val)
			{
				first = node_list.get(i-1);
				break;
			}
		}
		for(int i = length-2; i > -1; i--)
		{
			if (node_list.get(i).val > node_list.get(i+1).val)
			{
				second = node_list.get(i+1);
				break;
			}
		}
		int temp = first.val;
		first.val = second.val;
		second.val = temp;
	}
	
	public ArrayList<TreeNode> inorderDFS(TreeNode root, ArrayList<TreeNode> node_list)
	{
		if (root == null)
			return node_list;
		inorderDFS(root.left, node_list);
		node_list.add(root);
		inorderDFS(root.right, node_list);
		return node_list;
	}
	
	public void printList(ArrayList<TreeNode> node_list)
	{
		int length = node_list.size();
		for(int i = 0; i < length; i++)
		{
			System.out.println(node_list.get(i).val);
		}
	}
}
