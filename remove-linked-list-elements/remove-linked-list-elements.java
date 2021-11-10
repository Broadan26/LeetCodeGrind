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
    public ListNode removeElements(ListNode head, int target) 
    {
        if (head == null) // List does not exist
            return head;
        
        ListNode it = new ListNode(-1, head);
        head = it;
        while (it.next != null)
        {
            if (it.next.val == target)
                it.next = it.next.next;
            else
                it = it.next;
        }
        return head.next;
    }
}