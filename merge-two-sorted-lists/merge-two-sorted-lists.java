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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) 
    {
        // One of the lists is empty
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        
        // Assign a starting value to head
        ListNode head = null;
        if (l1.val <= l2.val)
        {
            head = l1;
            l1 = l1.next;
        }
        else
        {
            head = l2;
            l2 = l2.next;
        }
        
        // Iterate both lists
        ListNode iterator = head;
        while (l1 != null && l2 != null)
        {
            if (l1.val <= l2.val)
            {
                iterator.next = l1;
                l1 = l1.next;
            }
            else
            {
                iterator.next = l2;
                l2 = l2.next;
            }
            iterator = iterator.next;
        }
        
        // Iterate remaining lists
        while (l1 != null)
        {
            iterator.next = l1;
            l1 = l1.next;
            iterator = iterator.next;
        }
        while (l2 != null)
        {
            iterator.next = l2;
            l2 = l2.next;
            iterator = iterator.next;
        }
        
        return head;
    }
}