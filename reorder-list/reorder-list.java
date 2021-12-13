/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution 
{
    public void reorderList(ListNode head) 
    {
        // Nothing to alter
        if (head == null || head.next == null) return;
        
        // Find middle of the list using fast/slow pointers
        ListNode p1 = head;
        ListNode p2 = head;
        while (p2.next != null && p2.next.next != null)
        {
            p1 = p1.next;
            p2 = p2.next.next;
        }
        
        // Reverse the latter half of the linked list
        ListNode prev = p1;
        ListNode prevNext = p1.next;
        while (prevNext.next != null)
        {
            ListNode current = prevNext.next;
            prevNext.next = current.next;
            current.next = prev.next;
            prev.next = current;
        }
        
        // Alternate between front half and back half of list to reorder
        p1 = head;
        p2 = prev.next;
        while (p1 != prev)
        {
            prev.next = p2.next;
            p2.next = p1.next;
            p1.next = p2;
            p1 = p2.next;
            p2 = prev.next;
        }
    }
}