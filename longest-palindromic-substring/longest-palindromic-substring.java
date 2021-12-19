class Solution 
{
    public String longestPalindrome(String s) 
    {
        int length = s.length();
        int start = 0, end = 0;
        
        boolean[][] memo = new boolean[length][length];
        
        for (int i = length-1; i >= 0; i--)
            for (int j = i; j < length; j++)
            {
                memo[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 2 || memo[i+1][j-1]);
                
                if (memo[i][j] == true && j - i > end - start)
                {
                    start = i;
                    end = j;
                } 
            }
        return length == 0 ? "" : s.substring(start, end+1);
    }
}