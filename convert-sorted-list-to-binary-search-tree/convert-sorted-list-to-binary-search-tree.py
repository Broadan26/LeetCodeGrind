# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        current = head
        linked_list_to_sorted_list = []
        while current is not None: #Create a sorted list from the linked list
            linked_list_to_sorted_list.append(current.val)
            current = current.next

        return self.buildTree(linked_list_to_sorted_list, 0, len(linked_list_to_sorted_list) - 1)
    
    def buildTree(self, linked_list: list[int], low: int, high: int) -> TreeNode:
        if low > high: #End recursion
            return None
        mid = (low + high) // 2
        root = TreeNode(linked_list[mid]) #D&C to build the tree
        root.left = self.buildTree(linked_list, low, mid - 1)
        root.right = self.buildTree(linked_list, mid+1, high)
        return root