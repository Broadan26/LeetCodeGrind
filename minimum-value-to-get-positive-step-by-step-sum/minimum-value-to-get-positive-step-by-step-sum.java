class Solution 
{
    public int minStartValue(int[] nums) 
    {
        int startValue = 1;
        int currSum = 0;
        for (int i = 0; i < nums.length; i++)
        {
            currSum += nums[i];
            if (currSum < 1)
                startValue = Math.max(startValue, (currSum * -1)+1);
        }
        return startValue;
    }
}