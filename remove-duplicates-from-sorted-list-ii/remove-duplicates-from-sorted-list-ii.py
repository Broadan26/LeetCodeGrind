# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Given a linked list removes all nodes with duplicate values
        Returns the head of the original linked list
        '''
        #List is empty or only has a single node
        if not head or head.next is None:
            return head

        #List has more than 1 node, iterate and remove duplicates
        new_list = ListNode(0, head) #Create a new list with no duplicates
        prev = new_list
        while head: #While the old list exists, run through it
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val: #Skip past duplicates
                    head = head.next
                prev.next = head.next #Assign first unique to the new list
            else: #Unique val, keep moving
                prev = prev.next
            head = head.next #Move forward
        return new_list.next