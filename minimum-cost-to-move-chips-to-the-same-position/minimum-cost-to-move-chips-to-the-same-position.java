class Solution 
{
    public int minCostToMoveChips(int[] position) 
    {
        // Setup counters for chips in positions
        int odd = 0, even = 0;
        
        // Check each chip to find out which position it is in
        for (int chip : position)
        {
            if (chip % 2 == 0)
                even += 1;
            else
                odd += 1;
        }
        
        // Return the smaller pile
        return Math.min(odd, even);
    }
}