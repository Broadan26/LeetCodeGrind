class Solution 
{
    public int[] productExceptSelf(int[] nums) 
    {
        int[] answer = new int[nums.length];
        answer[0] = 1;
        
        // Accumulate products from left -> right
        for (int i = 1; i < nums.length; i++)
            answer[i] = answer[i-1] * nums[i-1];
        
        // Accumulate other products from right -> left
        int back = 1;
        for (int i = nums.length-1; i > -1; i--)
        {
            answer[i] *= back;
            back *= nums[i];
        }
        
        return answer;
    }
}