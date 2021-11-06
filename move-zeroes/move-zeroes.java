class Solution 
{
    public void moveZeroes(int[] nums) 
    {
        // Move all digits to front of the array
        int lastZero = 0;
        for (int i = 0; i < nums.length; i++)
            if (nums[i] != 0)
                nums[lastZero++] = nums[i];
        
        // Insert zeroes once last digit found
        for (int i = lastZero; i < nums.length; i++)
            nums[i] = 0;
    }
}