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
    public ListNode partition(ListNode head, int x) 
    {
        // Create dummy nodes to partition
        ListNode before = new ListNode(-1), after = new ListNode(-1);
        ListNode beforeIt = before, afterIt = after;
        
        // Iterate original list to partition
        while (head != null)
        {
            if (head.val < x)
            {
                beforeIt.next = head;
                beforeIt = beforeIt.next;
            }
            else
            {
                afterIt.next = head;
                afterIt = afterIt.next;
            }
            head = head.next;
        }
        
        // Remove potential cycle, remove dummy nodes
        afterIt.next = null;
        beforeIt.next = after.next;
        return before.next;
    }
}