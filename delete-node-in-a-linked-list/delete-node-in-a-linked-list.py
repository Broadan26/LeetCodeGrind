# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        '''
        Deletes a middle node in a linked list that is not a tail node
        Returns the updated node
        '''
        node.val = node.next.val
        node.next = node.next.next