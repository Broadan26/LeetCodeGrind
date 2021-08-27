# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Given a list of linked list heads, this combines them into a single linked list
        Returns the head of this new list
        '''
        list_of_nodes = []
        new_head = it = ListNode(0) # Create new head and iterator
        for list in lists: # Iterate the linked lists to build single list of values
            while list:
                list_of_nodes.append(list.val)
                list = list.next
        for item in sorted(list_of_nodes): # Sort the list and build new linked list
            it.next = ListNode(item)
            it = it.next
        return new_head.next