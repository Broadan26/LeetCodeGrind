class Solution 
{
    public int getMaxLen(int[] nums) 
    {
        if (nums.length < 1) // No array
            return 0;
        
        int maxLength = 0;
        int positives = 0, negatives = 0;
        for (int x : nums)
        {
            // Restart count
            if (x == 0)
            {
                positives = 0;
                negatives = 0;
            }
            // Increment positives, change negatives in negative seen before
            else if (x > 0)
            {
                positives++;
                negatives = negatives == 0 ? 0 : negatives+1;
            }
            // Swap negatives and positives and increment
            else
            {
                int swap = positives;
                positives = negatives == 0 ? 0 : negatives+1;
                negatives = swap+1;
            }
            maxLength = Math.max(maxLength, positives); // Store longest possible
        }
        return maxLength;
    }
}