class Solution 
{
    public String minRemoveToMakeValid(String s) 
    {
        // Create a stringbuilder to quickly edit the string s
        StringBuilder answer = new StringBuilder();
        
        // Create a stack to track parentheses
        Deque<Character> stack = new LinkedList<>();
        
        // Iterate the string and remove extra ')' parentheses
        // 0 -> s.length()
        for (char ch : s.toCharArray())
        {
            if (ch == '(')
            {
                stack.addLast(ch);
                answer.append(ch);
            }
            else if (ch == ')' && !stack.isEmpty())
            {
                answer.append(ch);
                stack.removeLast();
            }
            else if (ch == ')' && stack.isEmpty())
                continue;
            else
                answer.append(ch);
        }
        
        // Iterate the string again and remove extra '(' parentheses
        // answer.length() -> 0
        int i = answer.length()-1;
        while (!stack.isEmpty())
        {
            if (answer.charAt(i) == '(')
            {
                answer.setCharAt(i, ' ');
                stack.removeLast();
            }
            i--;
        }
        
        return answer.toString().replaceAll(" ", "");
    }
}