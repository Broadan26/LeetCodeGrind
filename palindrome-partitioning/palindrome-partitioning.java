class Solution 
{
    public List<List<String>> partition(String s) 
    {
        List<List<String>> answer = new ArrayList<>();
        generate(0, answer, new ArrayList<String>(), s);
        return answer;
    }
    
    private void generate(int start, List<List<String>> answer, List<String> current, String s)
    {
        // Base case to add partition to answer
        if (start >= s.length())
            answer.add(new ArrayList<String>(current));
        
        // Generate partitions with palindromes
        for (int end = start; end < s.length(); end++)
        {
            if (isPalindrome(s, start, end))
            {
                current.add(s.substring(start, end+1));
                generate(end+1, answer, current, s);
                current.remove(current.size()-1);
            }
        }
    }
    
    /* Check if string is a palindrome*/
    private boolean isPalindrome(String s, int start, int end)
    {
        while (start < end)
        {
            if (s.charAt(start) != s.charAt(end))
                return false;
            start++;
            end--;
        }
        return true;
    }
}