class Solution 
{
    public boolean increasingTriplet(int[] nums)
    {
        // Set a chain of values that are logically in order
        // If we ever find a 3rd increase, return true
        int i = Integer.MAX_VALUE, j = Integer.MAX_VALUE;
        for (int num : nums)
        {
            if (num <= i)
                i = num;
            else if (num <= j)
                j = num;
            else
                return true;
        }
        return false;
    }
    
    /*
    public boolean increasingTriplet(int[] nums) 
    {
        // Check all variations of i < j < k
        for (int i = 0; i < nums.length-2; i++)
            for (int j = i+1; j < nums.length-1; j++)
                for (int k = j+1; k < nums.length; k++)
                    if (nums[i] < nums[j] && nums[j] < nums[k])
                        return true;
        
        return false;
    }
    */
}