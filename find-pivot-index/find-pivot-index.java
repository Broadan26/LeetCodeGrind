class Solution 
{
    public int pivotIndex(int[] nums) 
    {
        int sum = 0, leftSum = 0;
        for (int num: nums) // Find total sum
            sum += num;
        
        // Look for point where leftSum matches half of total sum
        for (int i = 0; i < nums.length; i++)
        {
            if (leftSum == sum - leftSum - nums[i]) return i;
            leftSum += nums[i];
        }
        return -1;
    }
}