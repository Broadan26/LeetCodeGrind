class Solution 
{
    public int[] dailyTemperatures(int[] temperatures) 
    {
        if (temperatures.length < 1) // Impossible
            return new int[]{-1};
        
        // Create stack to remember temps, answer to store diff
        Deque<Integer> stack = new LinkedList<Integer>();
        int[] answer = new int[temperatures.length];
        
        for (int i = 0; i < temperatures.length; i++)
        {
            // Nothing on stack to compare with
            if (stack.size() < 1)
                stack.addFirst(i);
            
            // Current temperature hotter than previous
            else if (temperatures[i] > temperatures[stack.getFirst()])
            {
                while (!stack.isEmpty() && temperatures[i] > temperatures[stack.getFirst()])
                {
                    int index = stack.removeFirst();
                    answer[index] = i - index;
                }
                stack.addFirst(i);
            }
            // Current temperature is smaller than previous
            else
                stack.addFirst(i);
        }
        return answer;
    }
}