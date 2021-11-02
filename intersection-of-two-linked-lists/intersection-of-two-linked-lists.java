/**
 * Definition for singly-linked list.
 * public class ListNode {
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
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) 
    {
        // One list does not exist, no intersection
        if (headA == null)
            return null;
        if (headB == null)
            return null;
        
        // Find the length of each list
        int lengthA = 0, lengthB = 0;
        ListNode itA = headA, itB = headB;
        while (itA != null)
        {
            lengthA++;
            itA = itA.next;
        }
        while (itB != null)
        {
            lengthB++;
            itB = itB.next;
        }
        
        // Find the equivalent start point
        itA = headA;
        itB = headB;
        while (lengthA > lengthB)
        {
            itA = itA.next;
            lengthA--;
        }
        while (lengthB > lengthA)
        {
            itB = itB.next;
            lengthB--;
        }
        
        // Find the possible intersection
        while (lengthA > 0 && lengthB > 0)
        {
            if (itA == itB)
                return itA;
            itA = itA.next;
            itB = itB.next;
            lengthA--;
            lengthB--;
        }
        return null;
    }
}