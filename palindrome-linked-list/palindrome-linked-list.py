# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_list = []
        while head is not None: #Convert linked list to a list
            linked_list.append(head.val)
            head = head.next
        lo = 0
        hi = len(linked_list) - 1
        while lo < hi: #Check if list is a palindrome
            if linked_list[lo] != linked_list[hi]:
                return False
            hi -= 1
            lo += 1
        return True