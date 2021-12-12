class MyLinkedList 
{

    private ListNode head;
    private int length;
    
    public MyLinkedList() 
    {
        this.head = null;
        this.length = 0;
    }
    
    public int get(int index) 
    {
        // Return -1 if index not in range
        if (index >= this.length || index < 0) return -1;
        
        // Return value at the specified index
        ListNode pt = this.head;
        for (int i = 0; i < index; i++)
            pt = pt.next;
        
        return pt.val;
    }
    
    public void addAtHead(int val) 
    {
        // Create dummy node to hold value
        ListNode dummy = new ListNode(val);
        
        // Set dummy next to head and make it new head
        dummy.next = this.head;
        this.head = dummy;
        this.length += 1;
    }
    
    public void addAtTail(int val) 
    {
        // Create new node and update length
        ListNode temp = new ListNode(val);
        length += 1;
        
        // List is empty, add last node to head
        if (this.head == null) this.head = temp;
        
        // List is not empty, iterate to end and add it
        else
        {
            ListNode pt = this.head;
            while (pt.next != null)
                pt = pt.next;
            pt.next = temp;
        }
    }
    
    public void addAtIndex(int index, int val) 
    {
        // Do not add node if index > length
        if (index > this.length) return;
        
        // If index == length, add node to end of list
        else if (index == this.length) addAtTail(val);
        
        // If index == 0, add node to front of list
        else if (index == 0) addAtHead(val);
        
        // Iterate the list to the index
        else
        {
            ListNode pt = this.head;
            this.length += 1;
            for (int i = 0; i < index-1; i++)
                pt = pt.next;

            // Create new node and update positions
            ListNode temp = new ListNode(val);
            temp.next = pt.next;
            pt.next = temp;
        }
    }
    
    public void deleteAtIndex(int index) 
    {
        // Invalid range
        if (index >= this.length || index < 0) return;
        
        // Node to be deleted is the head
        else if (index == 0) this.head = this.head.next;
        
        // Iterate the list to the index
        else
        {
            ListNode pt = this.head;
            for (int i = 0; i < index-1; i++)
                pt = pt.next;

            // Delete the node
            pt.next = pt.next.next;
        }
        this.length -= 1;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */