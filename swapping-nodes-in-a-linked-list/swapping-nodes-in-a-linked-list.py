# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head: # No list
            return head
        first = last = head
        for node in range(1, k): # Find kth node
            first = first.next
        null_check = first
        while null_check.next: # Find kth from end starting at first
            last = last.next
            null_check = null_check.next
        first.val, last.val = last.val, first.val # Swap
        return head