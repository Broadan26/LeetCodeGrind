# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: #List is empty
            return None
        temp = headA
        lenA = 0
        while temp: #Find length of list A
            temp = temp.next
            lenA += 1
        temp = headB
        lenB = 0
        while temp: #Find length of list B
            lenB += 1
            temp = temp.next
        while lenA > lenB or lenB > lenA: #Shorten the longer list, intersection must exist in shorter list if it at all
            if lenA > lenB:
                headA = headA.next
                lenA -= 1
            else:
                headB = headB.next
                lenB -= 1
        while lenA > 0: #Look for intersection
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
                lenA -= 1
        return None