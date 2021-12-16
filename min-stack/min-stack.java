class MinStack 
{

    private List<Integer> mins;
    private List<Integer> stack;
    
    public MinStack() 
    {
        mins = new ArrayList<>();
        stack = new ArrayList<>();
    }
    
    /* Pushes the value on to the top of the stack*/
    public void push(int val) 
    {
        if (stack.isEmpty())
        {
            stack.add(val);
            mins.add(val);
        }
        else
        {
            if (val <= mins.get(mins.size()-1))
                mins.add(val);
            stack.add(val);
        }
    }
    
    /* Removes the top element from the stack*/
    public void pop() 
    {
        if (!stack.isEmpty())
        {
            int val = stack.remove(stack.size()-1);
            if (val == mins.get(mins.size()-1))
                mins.remove(mins.size()-1);
        }
    }
    
    /* Returns the top element of the stack */
    public int top() 
    {
        if (!stack.isEmpty())
        {
            return stack.get(stack.size()-1);
        }
        return -1;
    }
    
    /* Returns the smallest element present in the stack */
    public int getMin() 
    {
        if (!stack.isEmpty())
        {
            return mins.get(mins.size()-1);
        }
        return -1;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */