class MyQueue {

    private Deque<Integer> stack1;
    private Deque<Integer> stack2;
    
    public MyQueue() 
    {
        stack1 = new LinkedList<Integer>(); // Input
        stack2 = new LinkedList<Integer>(); // Output
    }
    
    public void push(int x) 
    {
        stack1.addFirst(x);
    }
    
    public int pop() 
    {
        peek();
        return stack2.removeFirst();
    }
    
    public int peek() 
    {
        if (stack2.size() == 0)
        {
            while(!(stack1.size() == 0))
                stack2.addFirst(stack1.removeFirst());
        }
        return stack2.getFirst();
    }
    
    public boolean empty() 
    {
        return stack1.size() == 0 && stack2.size() == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */