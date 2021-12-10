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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {
        // Create a dummy node and pointers to iterate the lists
        // Create a carry for summations resulting in values > 9
        ListNode dummy = new ListNode(-1);
        ListNode p1 = l1, p2 = l2, current = dummy;
        int carry = 0;
        
        while (p1 != null || p2 != null)
        {
            // Extract values and perform basic addition
            int l1Val = p1 != null ? p1.val : 0;
            int l2Val = p2 != null ? p2.val : 0;
            int val = l1Val + l2Val + carry;
            
            // Determine if there is a new carry
            carry = val > 9 ? 1 : 0;
            
            // Create new node for the value and move ahead to it
            current.next = new ListNode(val % 10);
            current = current.next;
            
            // Move forward the listnode pointers for next addition
            if (p1 != null) p1 = p1.next;
            if (p2 != null) p2 = p2.next;
        }
        
        // Check if there was a carry on final addition
        if (carry > 0)
            current.next = new ListNode(carry);
        
        return dummy.next;
    }
}