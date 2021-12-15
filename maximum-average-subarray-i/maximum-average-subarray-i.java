class Solution 
{
    public double findMaxAverage(int[] nums, int k) 
    {
        // Cannot find an average
        if (k > nums.length || nums.length < 1) return -1;
        
        // Find an initial max subarray average
        double max = 0, sum = 0;
        for (int start = 0; start < k; start++)
            sum += nums[start];
        max = sum;
        
        // Find all other max averages using a sliding window
        for (int i = k; i < nums.length; i++)
        {
            sum += nums[i]; // Add new last element
            sum -= nums[i-k]; // Remove old first element
            max = sum > max ? sum : max; // New max found or not
        }
        
        return max / k;
    }
}