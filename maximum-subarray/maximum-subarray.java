class Solution 
{
    public int maxSubArray(int[] nums) 
    {
        int maxSoFar = nums[0], maxEndingHere = nums[0];
        for (int i = 1; i < nums.length; i++)
        {
            maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]); //Check for new temp max
            maxSoFar = Math.max(maxSoFar, maxEndingHere); // Track single largest subarray
        }
        return maxSoFar;
    }
}