# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = jump = ListNode(0) # Create a temp head node
        dummy.next = left = right = head

        while True: # Run through the list
            count = 0
            while right and count < k: # Check to make sure reverse is possible
                right = right.next
                count += 1
            if count == k:
                prev, current = right, left
                for _ in range(k):
                    current.next, current, prev = prev, current.next, current # Reverse
                jump.next, jump, left = prev, left, right # Reconnect
            else:
                return dummy.next