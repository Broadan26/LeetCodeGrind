class Solution 
{
    public boolean isValid(String s) 
    {
        Deque<Character> stack = new LinkedList<Character>();
        for (int i = 0; i < s.length(); i++)
        {
            // Push left braces
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{')
                stack.push(s.charAt(i));
            // Pop equivalent right braces
            else if (!stack.isEmpty())
            {
                if (s.charAt(i) == ')' && stack.peek() == '(')
                    stack.pop();
                else if (s.charAt(i) == ']' && stack.peek() == '[')
                    stack.pop();
                else if (s.charAt(i) == '}' && stack.peek() == '{')
                    stack.pop();
                // Break if incorrect match
                else
                    return false;
            }
            else
                return false;
        }
        return stack.size() == 0;
    }
}