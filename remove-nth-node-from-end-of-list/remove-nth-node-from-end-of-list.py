# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: # List does not exist
            return None

        length = 0
        iterator = head
        while iterator is not None: # Find length of the list
            iterator = iterator.next
            length += 1
        
        remove_node = length - n # If node to be removed is head
        if remove_node == 0:
            head = head.next
            return head

        count = 0
        iterator = head
        while iterator: # Remove a node deeper in the list
            if count == remove_node-1:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count += 1
        return head