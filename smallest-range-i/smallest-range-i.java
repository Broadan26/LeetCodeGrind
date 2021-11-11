class Solution 
{
    public int smallestRangeI(int[] nums, int k) 
    {
        if (nums.length < 1) // No array
            return 0;
        
        // Find max and minimum values
        int maxVal = Integer.MIN_VALUE, minVal = Integer.MAX_VALUE;
        for(int i = 0; i < nums.length; i++)
        {
            if (nums[i] > maxVal) maxVal = nums[i];
            if (nums[i] < minVal) minVal = nums[i];
        }
        
        // Find relative difference between max and min
        int diff = ((maxVal - minVal)+1) / 2;
        
        return diff <= k ? 0 : (maxVal - minVal) - (2*k);
    }
}