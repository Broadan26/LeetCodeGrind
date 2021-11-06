class Solution 
{
    public int climbStairs(int n) 
    {
        if (n < 4) // Basic initial pattern
            return n;
        
        int possible = 3;
        int one_step = 2;
        int two_step = 3;
        for (int i = 3; i < n; i++)
        {
            possible = one_step + two_step;
            one_step = two_step;
            two_step = possible;
        }
        return possible;
    }
}