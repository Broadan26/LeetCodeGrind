class Solution 
{
    public boolean threeConsecutiveOdds(int[] arr) 
    {
        boolean odd1 = false, odd2 = false;
        for (int num : arr)
        {
            if (num % 2 == 0)
            {
                odd1 = false;
                odd2 = false;
            }
            else if (!odd1)
                odd1 = true;
            else if (!odd2)
                odd2 = true;
            else
                return true;
        }
        
        return false;
    }
}