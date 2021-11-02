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
    public ListNode deleteDuplicates(ListNode head) 
    {
        if (head == null) // No list exists
            return head;
        
        ListNode iterator = head;
        while (iterator != null)
        {
            if (iterator.next == null)
                break;
            if (iterator.val == iterator.next.val)
                iterator.next = iterator.next.next;
            else
                iterator = iterator.next;
        }
        return head;
    }
}