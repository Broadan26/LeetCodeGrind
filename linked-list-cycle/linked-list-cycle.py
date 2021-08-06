# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        Determines if a linked list contains a cycle
        Returns True if it does, otherwise false
        '''
        if not head: #List is empty
            return False
        slowP = head
        fastP = head.next
        while slowP is not fastP:
            if fastP is None or fastP.next is None or slowP is None:
                return False
            slowP = slowP.next
            fastP = fastP.next.next
        return True