class Solution 
{
    public int canCompleteCircuit(int[] gas, int[] cost) 
    {
        // Array lengths don't match
        if (gas.length != cost.length) return -1;
        
        int total = 0, current = 0, index = -1;
        for (int i = 0; i < gas.length; i++)
        {
            int diff = gas[i] - cost[i];
            total += diff;
            if (diff >= 0 && current == 0) // Potential starting point
            {
                index = i;
                current += diff;
            }
            else // Check for a broken start
            {
                current += diff;
                if (current < 0)
                {
                    current = 0;
                    index = -1;
                }
            }
        }
        return total >= 0 ? index : -1;
    }
}