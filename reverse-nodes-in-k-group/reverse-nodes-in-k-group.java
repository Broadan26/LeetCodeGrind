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
    public ListNode reverseKGroup(ListNode head, int k) 
    {
        // Find the length of the linked list
        int length = 0;
        for (ListNode node = head; node != null; length++, node = node.next);
        
        // Iterate the linked list while there are k nodes to reverse
        ListNode dummy = new ListNode(-1, head);
        for (ListNode prev = dummy, tail = head; length >= k; length -= k)
        {
            // Reverse the k nodes
            for (int i = 1; i < k; i++)
            {
                ListNode current = tail.next.next;
                tail.next.next = prev.next;
                prev.next = tail.next;
                tail.next = current;
            }
            // Update pointers for another iteration
            prev = tail;
            tail = tail.next;
        }
        
        return dummy.next;
    }
}