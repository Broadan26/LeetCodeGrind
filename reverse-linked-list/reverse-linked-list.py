# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        Reverses a singly linked list
        Returns the reversed list
        '''
        if not head: #No list
            return None
        new_list = None
        while head:
            new_node = ListNode(head.val, new_list)
            new_list = new_node
            head = head.next
        return new_list