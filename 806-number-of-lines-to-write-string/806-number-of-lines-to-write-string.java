class Solution 
{
    public int[] numberOfLines(int[] widths, String s) 
    {
        // Setup int[] to store answer
        int[] answer = {0, 0};
        
        // String s is empty
        if (s.length() < 1)
            return answer;
        
        // Track the remainder and update the lines
        int remain = 100;
        answer[0] = 1;
        
        // Run thru each char in the string s
        for (char ch: s.toCharArray())
        {
            int current = ch - 'a';
            if (remain - widths[current] < 0) // Next letter runs off the line
            {
                remain = 100;
                answer[0] += 1;
            }
            remain -= widths[current];
        }
        answer[1] = 100 - remain; // Update last line pixels
        return answer;
    }
}