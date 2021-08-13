# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Given a linked list, swaps every two adjacent nodes.
        Swaps the list nodes only, not the values.
        Returns the original list
        '''
        if not head or not head.next: #List is empty or has 1 node
            return head
        p1 = head
        phead = None
        last_p = None
        while p1 is not None and p1.next is not None: #List still has at least 2 elements to swap
            if not phead:
                phead = p1.next
            pnextnext = p1.next.next
            p1.next.next = p1
            if last_p:
                last_p.next = p1.next
            p1.next = pnextnext
            last_p = p1
            p1 = p1.next
        return phead