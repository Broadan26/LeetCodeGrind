# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        Traverses a singly linked list to find the middle node
        If odd, returns the middle node
        If even, returns the rightmost middle node
        '''
        if head is None:
            return None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next #Move fast 2
            slow = slow.next #Move slow 1
        return slow