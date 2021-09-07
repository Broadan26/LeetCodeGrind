# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        '''
        Given a linked list representing a binary number
        Returns the value of that binary number as an int
        '''
        num = 0
        while head is not None:
            if head.val == 1:
                num *= 2
                num += 1
            else:
                num *= 2
            head = head.next
        return num