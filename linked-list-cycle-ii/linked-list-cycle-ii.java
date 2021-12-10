/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution 
{
    public ListNode detectCycle(ListNode head) 
    {
        // No list exists
        if (head == null) return null;
        
        // Create hashset to store nodes previously seen
        HashSet<ListNode> listSet = new HashSet<>();
        
        // Iterate the list hashing nodes and checking if they have been seen
        // If node has been seen before, return it as cycle start
        ListNode it = head;
        while (it != null)
        {
            if (!listSet.contains(it))
                listSet.add(it);
            else
                return it;
            it = it.next;
        }
        
        return null;
    }
}