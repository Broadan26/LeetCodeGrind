class Solution 
{
    public int maxPower(String s) 
    {
        // Keep track of the current count & max counts of chars
        int count = 0, max = 0;
        char prev = ' ';
        
        // Iterate the entire string and count each contiguous letter
        for (int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            
            if (ch == prev) 
                count += 1;
            else
            {
                count = 1;
                prev = ch;
            }
            
            // Update the max count
            max = max < count ? count : max;
        }
        
        return max;
    }
}