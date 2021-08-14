# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p1 = head
        prev = None
        while p1:
            if p1.val == val:
                if p1 == head: #Still at head
                    p1 = p1.next
                    head = head.next
                else: #Not at head
                    prev.next = p1.next
                    p1 = p1.next
            else: #Move forward
                prev = p1
                p1 = p1.next
        return head