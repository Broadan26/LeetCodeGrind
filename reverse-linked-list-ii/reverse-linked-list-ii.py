# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: # No reversal occurs
            return head

        front = ListNode(None) # Create a temp front node if left is 1
        front.next = head
        it_front = front
        for i in range(left-1): # Move to start reversal
            it_front = it_front.next
        it_tail = it_front.next

        for i in range(right - left): # Reverse the interval
            temp = it_front.next # Create third node to store tail
            it_front.next = it_tail.next  # Reverse the connection
            it_tail.next = it_tail.next.next 
            it_front.next.next = temp 

        return front.next