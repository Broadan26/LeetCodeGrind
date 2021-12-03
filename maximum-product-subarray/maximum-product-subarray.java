class Solution 
{
    public int maxProduct(int[] nums) 
    {
        // Nothing to do
        if (nums.length < 1) return 0;
        
        // Run thru array of nums performing products
        int answer = nums[0], max = answer, min = answer;
        for (int i = 1; i < nums.length; i++)
        {
            // Swap the values because multiplying by a negative
            if (nums[i] < 0)
            {
                int temp = max;
                max = min;
                min = temp;
            }
            
            // The max/min produt of the number is either itself 
            // or the product of max/min & the potential answer
            max = Math.max(nums[i], max * nums[i]);
            min = Math.min(nums[i], min * nums[i]);
            
            // Check if new max could be potential answer
            answer = Math.max(answer, max);
        }
        
        return answer;
    }
}