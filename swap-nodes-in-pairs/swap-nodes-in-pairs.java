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
    public ListNode swapPairs(ListNode head) 
    {
        // Nothing to do be done
        if (head == null || head.next == null) return head;
        
        // Create dummy node to avoid null pointer issues with head
        ListNode dummy = new ListNode(-1, head);
        ListNode current = dummy;
        
        // Iterate the list and swap nodes in pairs if possible
        while (current.next != null && current.next.next != null)
        {
            // Assign nodes to be swapped
            ListNode p1 = current.next;
            ListNode p2 = current.next.next;
            
            // Swap
            p1.next = p2.next;
            current.next = p2;
            current.next.next = p1;
            
            // Iterate forward
            current = current.next.next;
        }
            
        return dummy.next;
    }
}