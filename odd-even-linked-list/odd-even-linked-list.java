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
    public ListNode oddEvenList(ListNode head) 
    {
        // Create dummy nodes to iterate through original list
        ListNode evens = new ListNode(-1), evenIt = evens;
        ListNode odds = new ListNode(-1), oddIt = odds;
        
        while (head != null)
        {
            // Build the odd list
            oddIt.next = head;
            head = head.next;
            oddIt = oddIt.next;
            oddIt.next = null;
            
            // Break if no more nodes
            if (head == null) break;
            
            // Build the even list
            evenIt.next = head;
            head = head.next;
            evenIt = evenIt.next;
            evenIt.next = null;
        }
        
        // Combine the two lists and return
        oddIt.next = evens.next;
        return odds.next;
    }
}