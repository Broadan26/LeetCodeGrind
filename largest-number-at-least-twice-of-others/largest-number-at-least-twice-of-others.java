class Solution 
{
    public int dominantIndex(int[] nums) 
    {
        // Find the maximum value and its index
        int maxIndex = 0, maxNum = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++)
        {
            maxIndex = (nums[i] > maxNum) ? i : maxIndex;
            maxNum = Math.max(maxNum, nums[i]);
        }
        
        // Compare maxNum with rest of array
        for (int i = 0; i < nums.length; i++)
            if (maxNum < 2 * nums[i] && i != maxIndex)
                return -1;
        
        return maxIndex;
    }
}