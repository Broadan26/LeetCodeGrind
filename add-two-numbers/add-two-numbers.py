# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        if l1 is None: #Handle case of empty lists
            return l2
        if l2 is None:
            return l1
        carry = 0
        head = l1
        p1 = l1
        p2 = l2
        prev = None
        while (p1 is not None and p2 is not None): #Both lists have remaining elements
            val1 = p1.val
            val2 = p2.val
            total = val1 + val2 + carry
            carry = total // 10 #Determine new carry
            total = total % 10 #Determine node value
            p1.val = total #Assign value to node

            prev = p1 #Keep previous node in case next is None
            p1 = p1.next
            p2 = p2.next
        while (p1 is not None and carry != 0): #l2 is empty
            total = p1.val + carry
            carry = total // 10
            total = total % 10
            p1.val = total
            prev = p1
            p1 = p1.next
        while (p2 is not None): #l1 is empty
            total = p2.val + carry
            carry = total // 10
            total = total % 10
            prev.next = ListNode(total)
            prev = prev.next
            p2 = p2.next
        if carry != 0: #l1 is empty, l2 is empty, carry is greater than 0
            prev.next = ListNode(carry)
        return head