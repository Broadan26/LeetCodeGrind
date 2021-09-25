# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # No list exists
            return None
        
        evenP = head.next
        oddP = head
        while evenP and evenP.next:
            temp = oddP.next
            oddP.next = evenP.next
            evenP.next = oddP.next.next
            oddP.next.next = temp

            oddP = oddP.next
            evenP = evenP.next
        return head